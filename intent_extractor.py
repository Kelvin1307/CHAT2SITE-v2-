# intent_extractor.py
import os
import json
import re
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",   # was openai/gpt-oss-20b
    temperature=0,
)

INTENT_PROMPT = """Extract high-level intent and key business information from the conversation.

STRICT RULES:
- Return ONLY valid JSON — no explanations, no markdown.
- For style_hint: summarise any colour/design preference in a short phrase. Set "" if none mentioned.

Return JSON in this exact format:
{
  "intent": "business_setup",
  "business_type": "",
  "core_services": [],
  "city": "",
  "contact_present": true,
  "style_hint": ""
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


def extract_intent(conversation: list) -> dict:
    text = "\n".join(conversation)

    prompt = f"""{INTENT_PROMPT}

Conversation:
{text}
"""

    response = llm.invoke(prompt)
    content = response.content.strip()

    try:
        return json.loads(content)
    except Exception:
        return safe_parse(content)
