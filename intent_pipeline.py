import json
from intent_extractor import extract_intent
from schema_generator import generate_schema

INPUT_FILE = "dataset.json"
OUTPUT_FILE = "dataset_with_predictions_direct.json"


def run_pipeline():
    with open(INPUT_FILE, "r") as f:
        data = json.load(f)

    results = []

    for sample in data:
        conversation_text = sample["conversation"]

        # Convert to list
        conversation = [
            c.strip()
            for c in conversation_text.split("User:")
            if c.strip()
        ]

        try:
            intent = extract_intent(conversation)
            prediction = generate_schema(conversation, intent)
        except Exception as e:
            print("Error:", e)
            prediction = {}

        sample["prediction"] = prediction
        results.append(sample)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=2)

    print("✅ Intent-based predictions generated!")


if __name__ == "__main__":
    run_pipeline()