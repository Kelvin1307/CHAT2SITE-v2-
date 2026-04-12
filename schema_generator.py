import os
import json
import re
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="openai/gpt-oss-20b",
    temperature=0
)

SCHEMA_PROMPT = """
Generate final website JSON using intent and conversation.

STRICT RULES:
- Return ONLY JSON
- No extra text

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

def safe_parse(output):
    output = output.replace("```json", "").replace("```", "").strip()
    match = re.search(r"\{.*\}", output, re.DOTALL)
    if not match:
        return {}
    try:
        return json.loads(match.group())
    except:
        return {}

def generate_schema(conversation: list, intent: dict) -> dict:
    text = "\n".join(conversation)

    prompt = f"""
{SCHEMA_PROMPT}

Intent:
{json.dumps(intent, indent=2)}

Conversation:
{text}
"""

    response = llm.invoke(prompt)
    return safe_parse(response.content)