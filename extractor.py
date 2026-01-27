# extractor.py
import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    groq_api_key="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",
    model_name="openai/gpt-oss-20b",
    temperature=0
)

SYSTEM_PROMPT = """
You are Chat2Site – Business Website Builder.

From the given conversation, extract structured website data.

Return ONLY valid JSON in this format:
{
  "business_name": "",
  "business_type": "",
  "tagline": "",
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
