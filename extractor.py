# extractor.py
import os
import json
import re
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),   # was GROQ_API_KEY2 (wrong key name)
    model_name="llama-3.3-70b-versatile",      # was openai/gpt-oss-20b (causes BadRequestError)
    temperature=0,
)

SYSTEM_PROMPT = """You are Chat2Site – Business Website Builder.

Extract structured data from the conversation.

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


def safe_parse(output: str) -> dict:
    output = output.replace("```json", "").replace("```", "").strip()
    match = re.search(r"\{.*\}", output, re.DOTALL)
    if not match:
        return {}
    try:
        return json.loads(match.group())
    except json.JSONDecodeError:
        return {}


def extract_website_json(conversation: list) -> dict:
    joined_text = "\n".join(conversation)

    prompt = f"""{SYSTEM_PROMPT}

Conversation:
{joined_text}
"""

    response = llm.invoke(prompt)
    content = response.content.strip()

    try:
        return json.loads(content)
    except Exception:
        parsed = safe_parse(content)
        if parsed:
            return parsed
        raise ValueError("LLM did not return valid JSON")
