# tele.py
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from extractor import extract_website_json
from renderer import render_portfolio_site
from deployer import deploy_site

SYSTEM_START = (
    "👋 I’ll help you create a business website.\n"
    "First — what’s your business name?"
)

def start(update: Update, context: CallbackContext):
    context.user_data["conversation"] = []
    update.message.reply_text(SYSTEM_START)

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.strip()

    # Publish trigger
    if text.lower() in {"publish", "publish,free"}:
        update.message.reply_text("⚙️ Generating your website...")
        publish(update, context)
        return

    # Store raw conversation
    conversation = context.user_data.setdefault("conversation", [])
    conversation.append(text)

    # Ask next question using LLM lightly
    update.message.reply_text("Got it 👍 Please continue.")

def publish(update: Update, context: CallbackContext):
    conversation = context.user_data.get("conversation", [])

    # --- STEP 1: Extract JSON ---
    website_json = extract_website_json(conversation)

    # --- STEP 2: Render HTML ---
    output_dir = render_portfolio_site(website_json)

    # --- STEP 3: Deploy ---
    live_url = deploy_site(output_dir)

    # --- STEP 4: Respond ---
    update.message.reply_text(f"🎉 Your website is live:\n{live_url}")

def run_bot(token: str):
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    print("🤖 Chat2Site Telegram bot running...")
    updater.start_polling()
    updater.idle()
