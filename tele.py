# tele.py
import sys
import pytz

# ── APScheduler timezone monkey-patch (Python 3.9+ / zoneinfo compat) ───────
try:
    import apscheduler.util

    def _dummy_astimezone(obj):
        if obj is None:
            return pytz.utc
        if hasattr(obj, "localize"):
            return obj
        name = getattr(obj, "key", None) or getattr(obj, "zone", None) or str(obj)
        try:
            return pytz.timezone(name)
        except Exception:
            return pytz.utc

    apscheduler.util.astimezone = _dummy_astimezone
except ImportError:
    pass

import json
import os
import re
import asyncio
import functools

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from langchain_groq import ChatGroq
from combiner import combine_json
from renderer3 import render_page
from deployer import deploy_site

load_dotenv()

# ── Token & API key validation ───────────────────────────────────────────────
token = os.getenv("TELEGRAM_BOT_TOKEN")
if not token:
    raise RuntimeError("Missing TELEGRAM_BOT_TOKEN")

key = os.getenv("GROQ_API_KEY2")
if not key:
    raise RuntimeError("GROQ_API_KEY is missing.")
if not key.startswith("gsk_"):
    raise RuntimeError("GROQ_API_KEY looks invalid.")

# ── Constants ────────────────────────────────────────────────────────────────
SYSTEM_START = (
    "👋 I'll help you create a business website.\n"
    "Tell me about your business, please."
)

CONVO_PROMPT = """You are Chat2Site, a friendly and helpful website builder assistant.

Your role is to have a natural conversation with the user about their business and gradually collect the information needed to build their website. Be warm, encouraging, and conversational—not robotic.

CONVERSATION STYLE:
- Be genuinely interested in what the user shares.
- Acknowledge their input naturally before moving forward.
- Use friendly language ("Great!", "That sounds amazing!", "I love that!").
- Break up requests naturally—don't feel pressured to ask all questions at once.
- If they volunteer information, confirm it and move on without redundant questions.
- Be flexible and adaptive to what they share.
- Respond ONLY with plain conversational text. No JSON, no structured data, no function calls.

INFORMATION TO COLLECT (internally, not shared with the user):
  business_name, business_type, services (3-6 items), city, phone or email,
  color_theme (optional), design_style (optional)

CONVERSATION FLOW:
1. Start — Listen to their business. Ask natural follow-up questions.
2. Explore — Understand services, uniqueness, audience.
3. Contact — Get phone and/or email in a friendly way.
4. Style (optional) — Ask once about preferred colours or design style.
   - If they say "I don't know", "no idea", "up to you", or similar → acknowledge and move on. DO NOT ask again.
   - If they give a preference → confirm it and move on.
5. Finalize — When you have core data (name, type, services, city, one contact), guide them to publish.

KEY BEHAVIORS:
- Never ask the same question twice.
- Once a field is confirmed, do not revisit it.
- Keep replies short — 1-2 sentences is ideal.
- Offer gentle examples when the user is unsure.
- Do NOT output JSON or any structured data to the user.
- Change to the user's language if they stop responding in English.
- Style/colour questions are OPTIONAL — missing style never blocks website creation.

SPECIAL INSTRUCTION:
When the user says "publish", "generate", "go ahead", "launch", or "create site", reply with exactly:
"🚀 Generating your website now. This will take a few seconds."

Remember: You're building a relationship and helping them create something amazing.
"""

# ── Extraction schema (used by LLM to pull structured data from transcript) ──
SYSTEM_PROMPT = """You are Chat2Site – Business Website Builder.

Extract structured data from the conversation below.

STRICT RULES:
- Return ONLY valid JSON — no explanations, no markdown, no trailing commas.
- Leave a field as an empty string "" or empty list [] if it cannot be inferred.
- For color_theme: capture any mentioned colour preference (e.g. "blue and white", "earthy tones"). Set "" if the user said they don't know or gave no preference.
- For design_style: capture any style keywords (e.g. "modern", "elegant", "minimalist", "bold"). Set "" if unknown or not mentioned.

Return JSON in this exact format:
{
  "business_name": "",
  "business_type": "",
  "services": [],
  "city": "",
  "email": "",
  "phone": "",
  "color_theme": "",
  "design_style": ""
}
"""

# ── LLM setup ────────────────────────────────────────────────────────────────
def setup_llm() -> ChatGroq:
    """Initialize and return the ChatGroq LLM instance."""
    return ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        # llama-3.3-70b-versatile is reliable, follows system prompts, and does
        # NOT call tools when not instructed to — avoiding the 400 BadRequestError.
        model_name="llama-3.3-70b-versatile",
        temperature=0,
    )

llm = setup_llm()

# ── Helpers ──────────────────────────────────────────────────────────────────
def safe_parse(output: str) -> dict:
    """Strip markdown fences and parse the first JSON object found."""
    output = output.replace("```json", "").replace("```", "").strip()
    match = re.search(r"\{.*\}", output, re.DOTALL)
    if not match:
        return {}
    try:
        return json.loads(match.group())
    except json.JSONDecodeError:
        return {}


def extract_website_json(conversation: list) -> dict:
    """Ask the LLM to extract structured website data from the conversation."""
    joined_text = "\n".join(conversation)
    prompt = f"{SYSTEM_PROMPT}\n\nConversation:\n{joined_text}"
    response = llm.invoke(prompt)
    content = response.content.strip()

    # Try strict parse first, then regex fallback
    try:
        return json.loads(content)
    except Exception:
        parsed = safe_parse(content)
        if parsed:
            return parsed
        raise ValueError("LLM did not return valid JSON")


def is_website_data_complete(data: dict) -> bool:
    """
    Core fields (name, type, services, city) + at least one contact method.
    Style fields (color_theme, design_style) are OPTIONAL.
    """
    required = ["business_name", "business_type", "services", "city"]
    if not all(data.get(field) for field in required):
        return False
    return bool(data.get("phone")) or bool(data.get("email"))


def _run_sync(fn, *args):
    """
    Run a synchronous callable in the default thread-pool executor.
    Returns a coroutine suitable for `await`.
    """
    loop = asyncio.get_event_loop()
    return loop.run_in_executor(None, functools.partial(fn, *args))


# ── Async handlers ───────────────────────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /start — reset conversation state and greet the user."""
    context.user_data["conversation"] = [
        {"role": "assistant", "content": SYSTEM_START}
    ]
    context.user_data["style_asked"] = False  # track whether we asked about style
    await update.message.reply_text(SYSTEM_START)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle all non-command text messages."""
    user_text = update.message.text.strip()
    conversation = context.user_data.setdefault("conversation", [])

    # Store user message
    conversation.append({"role": "user", "content": user_text})

    # ── Smart publish detection ──────────────────────────────────────────────
    publish_triggers = {"publish", "generate", "go ahead", "launch", "create site"}
    if any(word in user_text.lower() for word in publish_triggers):
        await update.message.reply_text(
            "🚀 Generating your website now. This will take a few seconds."
        )
        await publish(update, context)
        return

    # ── Trim history (prevents token overflow) ───────────────────────────────
    MAX_HISTORY = 18
    trimmed_history = conversation[-MAX_HISTORY:]

    # ── Hidden fulfillment check ─────────────────────────────────────────────
    extra_system: list[dict] = []
    try:
        transcript = "\n".join(
            msg["content"] for msg in conversation if msg["role"] == "user"
        )
        website_data = await _run_sync(extract_website_json, [transcript])

        if is_website_data_complete(website_data):
            extra_system.append({
                "role": "system",
                "content": (
                    "✅ All required website details have been collected. "
                    "Do NOT ask any more questions about the business. "
                    "Warmly confirm everything is ready and ask the user to say 'publish' or 'go ahead' to launch their site."
                ),
            })
        else:
            # Style nudge: only ask once, only after core fields are mostly filled
            style_filled = bool(website_data.get("color_theme")) or bool(website_data.get("design_style"))
            style_asked = context.user_data.get("style_asked", False)
            core_mostly_done = bool(website_data.get("business_name")) and bool(website_data.get("services"))

            if core_mostly_done and not style_filled and not style_asked:
                context.user_data["style_asked"] = True
                extra_system.append({
                    "role": "system",
                    "content": (
                        "Core business info is mostly collected. "
                        "If you haven't yet, gently ask once about preferred colour palette or design style. "
                        "If the user says they don't know or don't mind, accept that and move on immediately — do NOT ask again."
                    ),
                })
    except Exception as e:
        print(f"⚠️ Hidden fulfillment check error: {e}")

    # ── Build messages & call LLM ────────────────────────────────────────────
    messages = [
        {"role": "system", "content": CONVO_PROMPT},
        *extra_system,
        *trimmed_history,
    ]

    response = await _run_sync(llm.invoke, messages)
    bot_reply = response.content

    conversation.append({"role": "assistant", "content": bot_reply})
    await update.message.reply_text(bot_reply)


async def publish(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Run the 4-step website generation and deployment pipeline."""
    conversation = context.user_data.get("conversation", [])
    transcript = "\n".join(
        msg["content"] for msg in conversation if msg["role"] == "user"
    )

    try:
        status_msg = await update.message.reply_text(
            "⚙️ Step 1/4: Extracting business details from conversation..."
        )

        # Step 1 – Extract JSON (includes color_theme, design_style)
        website_json = await _run_sync(extract_website_json, [transcript])

        # Step 2 – Combine / enrich JSON
        await status_msg.edit_text(
            "🪄 Step 2/4: Generating detailed site content, copy, and layout schemas..."
        )
        website_json = await _run_sync(combine_json, website_json)

        # Step 3 – Render template (smart strategy uses business_type + style)
        await status_msg.edit_text(
            "🎨 Step 3/4: Choosing the matching design style and rendering template..."
        )
        output_dir = await _run_sync(
            lambda: render_page(website_json, output_dir="site_output", strategy="smart")
        )

        # Step 4 – Deploy
        await status_msg.edit_text(
            "🚀 Step 4/4: Deploying your website live on the web..."
        )
        live_url = await _run_sync(deploy_site, output_dir)

        await update.message.reply_text(
            f"🎉 Your website is live!\n{live_url}"
        )

    except Exception as e:
        print(f"❌ Error during publication flow: {e}")
        await update.message.reply_text(
            f"❌ Sorry, something went wrong while building your site:\n{e}"
        )


# ── Entry point ──────────────────────────────────────────────────────────────
def main() -> None:
    """Build the Application, register handlers, and start polling."""
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Chat2Site Telegram bot running...")
    app.run_polling()


if __name__ == "__main__":
    main()
