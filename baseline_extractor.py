import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import re

def safe_parse(output):
    output = output.replace("```json", "").replace("```", "").strip()
    match = re.search(r"\{.*\}", output, re.DOTALL)
    if not match:
        return {}
    try:
        return json.loads(match.group())
    except:
        return {}
    
load_dotenv()


llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY3"),
    model_name="openai/gpt-oss-20b",
    temperature=0
)

BASELINE_PROMPT = """
Extract business details from the conversation and return JSON.
Guidelines:
- services should be a list of items mentioned
- Extract email and phone even if written with words like "contact", "reach", or "phone"
- Do not miss information if it is present
- Keep values concise and accurate
- If something is not mentioned, return empty string ""

Conversation:
{conversation}


"""

def extract_baseline(conversation: list) -> dict:
    text = "\n".join(conversation)

    prompt = f"""
{BASELINE_PROMPT}

Conversation:
{text}
"""

    response = llm.invoke(prompt)

    return safe_parse(response.content)