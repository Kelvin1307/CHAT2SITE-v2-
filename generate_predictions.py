import json
from extractor import extract_website_json

INPUT_FILE = "dataset.json"
OUTPUT_FILE = "dataset_with_predictions.json"


def generate_predictions():
    with open(INPUT_FILE, "r") as f:
        data = json.load(f)

    new_data = []

    for sample in data:
        conversation_text = sample["conversation"]

        # Convert string → list
        conversation = conversation_text.split("User:")
        conversation = [c.strip() for c in conversation if c.strip()]

        try:
            prediction = extract_website_json(conversation)
        except Exception as e:
            print("Error:", e)
            prediction = {}

        sample["prediction"] = prediction
        new_data.append(sample)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(new_data, f, indent=2)

    print("✅ Predictions generated!")


if __name__ == "__main__":
    generate_predictions()