import json
from baseline_extractor import extract_baseline

INPUT_FILE = "dataset.json"
OUTPUT_FILE = "dataset_with_predictions_baseline.json"


def run_baseline():
    with open(INPUT_FILE, "r") as f:
        data = json.load(f)

    results = []

    for sample in data:
        conversation_text = sample["conversation"]

        # Convert string → list (same as your main pipeline)
        conversation = [
            c.strip()
            for c in conversation_text.split("User:")
            if c.strip()
        ]

        try:
            def normalize(pred):
                return {
                    "business_name": pred.get("business_name", ""),
                    "business_type": pred.get("business_type", pred.get("type", "")),
                    "services": pred.get("services", []),
                    "city": pred.get("city", pred.get("location", "")),
                    "email": pred.get("email", pred.get("contact_information", {}).get("email", "")),
                    "phone": pred.get("phone", pred.get("contact_information", {}).get("phone", ""))
                }

            raw_pred = extract_baseline(conversation)
            prediction = normalize(raw_pred)
        except Exception as e:
            print("Error:", e)
            prediction = {}  # baseline allowed to fail

        sample["prediction"] = prediction
        results.append(sample)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=2)

    print("✅ Baseline predictions generated!")


if __name__ == "__main__":
    run_baseline()