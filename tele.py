# tele.py
import json
import os
import re
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from langchain_groq import ChatGroq
from combiner import combine_json
from extractor import extract_website_json
from renderer3 import render_page
from deployer import deploy_site

load_dotenv()
token = os.getenv("TELEGRAM_BOT_TOKEN")
if not token:
    raise RuntimeError("Missing TELEGRAM_BOT_TOKEN")
SYSTEM_START = (
    "👋 I’ll help you create a business website.\n"
    "Tell me about your business,please."
)

key = os.getenv("GROQ_API_KEY")

if not key:
    raise RuntimeError("GROQ_API_KEY is missing.")

if not key.startswith("gsk_"):
    raise RuntimeError("GROQ_API_KEY looks invalid.")


CONVO_PROMPT = """You are Chat2Site, a friendly and helpful website builder assistant.

Your role is to have a natural conversation with the user about their business and gradually collect the information needed to build their website. Be warm, encouraging, and conversational—not robotic.

CONVERSATION STYLE:
- Be genuinely interested in what the user shares.
- Acknowledge their input naturally before moving forward.
- Use friendly language ("Great!", "That sounds amazing!", "I love that!").
- Break up requests naturally—don't feel pressured to ask all questions at once.
- If they volunteer information, confirm it and move on without redundant questions.
- Be flexible and adaptive to what they share.
- Do NOT use any tools, function calls, or structured outputs. Respond only with natural conversational text.

INFORMATION YOU NEED TO GATHER (internally):
{
  "business_name": "Name of the business",
  "business_type": "Type/category of business",
  "services": ["List of 3-6 services or products offered"],
  "city": "Location/city",
  "email": "Business email",
  "phone": "Business phone number"
}

CONVERSATION FLOW:
1. **Start**: Listen to what business they run. Ask follow-up questions naturally.
2. **Explore**: Understand their services, what makes them special, who they serve.
3. **Contact**: Get their contact details in a friendly way.
4. **Brand**: Ask about color preferences and design style if it feels natural.
5. **Finalize**: When you have enough info, suggest they're ready to generate their site.

KEY BEHAVIORS:
- Never ask the same question twice.
- If a field is complete, move on without revisiting it.
- Keep responses short and conversational (1-2 sentences usually).
- If the user is unsure, offer gentle suggestions or examples.
- DON'T output JSON or structured data to the user.
- DON'T be formulaic—sound like a real person having a conversation.
- If all required fields are collected, naturally guide them to publish.

SPECIAL INSTRUCTION:
If the user says "publish", "generate", "go ahead", or "launch", respond with:
"🚀 Generating your website now. This will take a few seconds."

Remember: You're building a relationship and helping them create something amazing, not filling out a form.
"""


def setup_llm():
    """Initialize and return the ChatGroq LLM instance."""
    return ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="openai/gpt-oss-20b",
        temperature=0
    )

llm = setup_llm()

EXTRACTION_PROMPT = """
You are a JSON extraction helper. Extract structured website data from the conversation below and return ONLY valid JSON matching this schema:
{{
  "business_name": "",
  "business_type": "",
  "services": [],
  "city": "",
  "email": "",
  "phone": ""
}}

Conversation:
{conversation}
"""


def safe_parse(output: str) -> dict:
    output = output.replace("```json", "").replace("```", "").strip()
    match = re.search(r"\{.*\}", output, re.DOTALL)
    if not match:
        return {}
    try:
        return json.loads(match.group())
    except json.JSONDecodeError:
        return {}


SYSTEM_PROMPT = """
You are Chat2Site – Business Website Builder.

Extract structured data from the conversation.

STRICT RULES:
- Return ONLY JSON
- Do NOT add explanations
- Do NOT add text before or after JSON
- Ensure valid JSON format (no trailing commas)

Format:
{
  "business_name": "",
  "business_type": "",
  "services": [],
  "city": "",
  "email": "",
  "phone": ""
}
"""

def extract_website_json(conversation: list) -> dict:
    # Explicit traversal
    joined_text = "\n".join(conversation)

    prompt = f"""
{SYSTEM_PROMPT}

Conversation:
{joined_text}
"""

    response = llm.invoke(prompt)

    try:
        return json.loads(response.content)
    except Exception:
        raise ValueError("LLM did not return valid JSON")



def is_website_data_complete(data: dict) -> bool:
    required_fields = ["business_name", "business_type", "services", "city"]
    if not all(data.get(field) for field in required_fields):
        return False
    contact_ok = bool(data.get("phone")) or bool(data.get("email"))
    return contact_ok


def start(update: Update, context: CallbackContext):
    context.user_data["conversation"] = [
        {"role": "assistant", "content": SYSTEM_START}
    ]
    context.user_data["website_data"] = {
    "business_name": None,
    "business_type": None,
    "location": None,
    "offerings": None,
    "target_area": None,
    "phone": None,
    "email": None,
    "brand_style": None,
    "socials": None
}

    update.message.reply_text(SYSTEM_START)

def handle_message(update: Update, context: CallbackContext):
    user_text = update.message.text.strip()



    conversation = context.user_data.setdefault("conversation", [])

    # Store user message
    conversation.append({"role": "user", "content": user_text})

    # ---- SMART PUBLISH DETECTION ----
    publish_words = {"publish", "generate", "go ahead", "launch", "create site"}

    if any(word in user_text.lower() for word in publish_words):
        update.message.reply_text("🚀 Generating your website now. This will take a few seconds.")
        publish(update, context)
        return

    # ---- TRIM HISTORY (prevents token overflow) ----
    MAX_HISTORY = 18
    trimmed_history = conversation[-MAX_HISTORY:]

    # ---- HIDDEN FULFILLMENT CHECK ----
    transcript = "\n".join(msg["content"] for msg in conversation if msg["role"] == "user")
    website_data = extract_website_json([transcript])
    extra_system = []
    if is_website_data_complete(website_data):
        extra_system.append({
            "role": "system",
            "content": "All required website details are already collected or nearly complete. Ask only for the confirmation of thefinal publish question."
        })

    # ---- BUILD MESSAGES ----
    messages = [
        {"role": "system", "content": CONVO_PROMPT},
        *extra_system,
        *trimmed_history
    ]

    # ---- CALL LLM ----
    response = llm.invoke(messages)
    bot_reply = response.content

    # Store assistant reply
    conversation.append({"role": "assistant", "content": bot_reply})

    # Send to Telegram
    update.message.reply_text(bot_reply)


def publish(update: Update, context: CallbackContext):
    conversation = context.user_data.get("conversation", [])

    transcript = "\n".join(
        msg["content"] for msg in conversation if msg["role"] == "user"
    )

    website_json = extract_website_json(transcript)
    website_json = combine_json(website_json)


    # --- STEP 2: Render HTML ---
    output_dir = render_page(website_json)

    # --- STEP 3: Deploy ---
    live_url = deploy_site(output_dir)

    # --- STEP 4: Respond ---
    update.message.reply_text(f"🎉 Your website is live:\n{live_url}")

def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    print("🤖 Chat2Site Telegram bot running...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
