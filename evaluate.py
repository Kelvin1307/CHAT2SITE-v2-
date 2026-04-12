import json

REQUIRED_FIELDS = ["business_name", "business_type", "services", "city", "email", "phone"]


# -------------------------------
# Helper Functions
# -------------------------------

def normalize(value):
    if isinstance(value, str):
        return value.strip().lower()
    if isinstance(value, list):
        return sorted([v.strip().lower() for v in value])
    return value


def field_exists(field, data):
    return field in data and data[field] != ""


# -------------------------------
# FCS: Field Coverage Score
# -------------------------------

def compute_fcs(gt, pred):
    total = len(REQUIRED_FIELDS)
    present = sum([1 for f in REQUIRED_FIELDS if field_exists(f, pred)])
    return present / total


# -------------------------------
# FCR: Field Correctness Rate
# -------------------------------

def compute_fcr(gt, pred):
    correct = 0
    total = 0

    for f in REQUIRED_FIELDS:
        if field_exists(f, gt):
            total += 1

            if f in pred:
                if normalize(gt[f]) == normalize(pred[f]):
                    correct += 1

    return correct / total if total > 0 else 0


# -------------------------------
# SPS: Schema Precision Score
# -------------------------------

def compute_sps(pred):
    pred_fields = set(pred.keys())
    required_fields = set(REQUIRED_FIELDS)

    correct_fields = pred_fields.intersection(required_fields)
    extra_fields = pred_fields - required_fields

    if len(pred_fields) == 0:
        return 0

    return len(correct_fields) / (len(correct_fields) + len(extra_fields))


# -------------------------------
# MAIN EVALUATION
# -------------------------------

def evaluate(dataset):
    total_fcs = 0
    total_fcr = 0
    total_sps = 0

    n = len(dataset)

    for sample in dataset:
        gt = sample["ground_truth"]
        pred = sample["prediction"]

        fcs = compute_fcs(gt, pred)
        fcr = compute_fcr(gt, pred)
        sps = compute_sps(pred)

        total_fcs += fcs
        total_fcr += fcr
        total_sps += sps

    print("----- FINAL SCORES -----")
    print(f"FCS: {total_fcs / n:.4f}")
    print(f"FCR: {total_fcr / n:.4f}")
    print(f"SPS: {total_sps / n:.4f}")


# -------------------------------
# LOAD DATASET
# -------------------------------

if __name__ == "__main__":
    with open("dataset_with_predictions_baseline.json", "r") as f:
        data = json.load(f)

    evaluate(data)