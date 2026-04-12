# extractor.py
import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY2"),
    model_name="openai/gpt-oss-20b",
    temperature=0
)

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
