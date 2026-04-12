# combiner.py

import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# ------------------ LLM SETUP ------------------
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="openai/gpt-oss-20b",
    temperature=0
)

# ------------------ TARGET TEMPLATE ------------------

with open("data2.json", "r", encoding="utf-8") as f:
    TARGET_JSON = json.load(f)


# ------------------ PROMPT ------------------

COMBINER_PROMPT = """
You are a JSON combiner and UI data generator.

You receive:
1. A PARTIAL business JSON (user data)
2. A TARGET website JSON structure

Your job:
- Merge both
- NEVER delete existing user values
- Fill ALL missing fields intelligently
- Ensure NO field is empty
- Generate realistic, professional content where missing

Rules:
- Keep structure EXACTLY like target
- If user data exists → use it
- If missing → generate high-quality defaults
- Do NOT leave empty arrays or empty strings
- Do NOT skip any keys
- Output ONLY valid JSON

Make sure:
- nav has at least 4 items
- products has at least 2 items
- categories has at least 3
- services has title, description, features, stats
- footer is complete
"""

# ------------------ MAIN FUNCTION ------------------

def combine_json(primary_json: dict) -> dict:
    prompt = f"""
PRIMARY JSON:
{json.dumps(primary_json, indent=2)}

TARGET STRUCTURE:
{json.dumps(TARGET_JSON, indent=2)}

{COMBINER_PROMPT}
"""

    response = llm.invoke(prompt)

    try:
        return json.loads(response.content) 
        print(json.dumps(final_json, indent=2))
        
    except Exception as e:
        print("❌ JSON parsing failed")
        print(response.content)
        raise e


# ------------------ TEST ------------------

if __name__ == "__main__":
    sample_primary = {
        "business_name": "Kelvin Cakes",
        "business_type": "store",
        "services_or_products": ["Custom Cakes", "Wedding Cakes"],
        "contact": {
            "phone": "+919999999999",
            "email": "kelvin@email.com"
        }
    }

    final_json = combine_json(sample_primary)

    print(json.dumps(final_json, indent=2))