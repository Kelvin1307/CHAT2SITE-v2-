# baseline_extractor.py
import os
import json
import re
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),   # was GROQ_API_KEY3 (wrong key name)
    model_name="llama-3.3-70b-versatile",      # was openai/gpt-oss-20b
    temperature=0,
)

BASELINE_PROMPT = """Extract business details from the conversation and return JSON.

Guidelines:
- services should be a list of items mentioned.
- Extract email and phone even if written with words like "contact", "reach", or "phone".
- Do not miss information if it is present.
- Keep values concise and accurate.
- If something is not mentioned, return empty string "".
- For color_theme: capture any colour preferences mentioned. Set "" if none.
- For design_style: capture style keywords (e.g. "modern", "minimalist"). Set "" if none.

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


def extract_baseline(conversation: list) -> dict:
    text = "\n".join(conversation)

    prompt = BASELINE_PROMPT.format(conversation=text)

    response = llm.invoke(prompt)
    content = response.content.strip()

    try:
        return json.loads(content)
    except Exception:
        return safe_parse(content)