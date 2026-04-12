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

INTENT_PROMPT = """
Extract high-level intent and key business information.

STRICT RULES:
- Return ONLY JSON
- No explanations

Format:
{
  "intent": "business_setup",
  "business_type": "",
  "core_services": [],
  "city": "",
  "contact_present": true
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

def extract_intent(conversation: list) -> dict:
    text = "\n".join(conversation)

    prompt = f"""
{INTENT_PROMPT}

Conversation:
{text}
"""

    response = llm.invoke(prompt)
    return safe_parse(response.content)
