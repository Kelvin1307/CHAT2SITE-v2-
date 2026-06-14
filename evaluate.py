import json

# Core fields that MUST be present for a valid website prediction
REQUIRED_FIELDS = ["business_name", "business_type", "services", "city", "email", "phone"]

# Optional fields — captured when available, scored separately
OPTIONAL_FIELDS = ["color_theme", "design_style"]


# -------------------------------
# Helper Functions
# -------------------------------

def normalize(value):
    if isinstance(value, str):
        return value.strip().lower()
    if isinstance(value, list):
        return sorted([v.strip().lower() for v in value if isinstance(v, str)])
    return value


def field_exists(field, data):
    val = data.get(field)
    if val is None or val == "" or val == []:
        return False
    return True


# -------------------------------
# FCS: Field Coverage Score
# Measures how many required fields are present in the prediction
# -------------------------------

def compute_fcs(gt, pred):
    total = len(REQUIRED_FIELDS)
    present = sum(1 for f in REQUIRED_FIELDS if field_exists(f, pred))
    return present / total


# -------------------------------
# FCR: Field Correctness Rate
# Measures how accurate present fields are vs ground truth
# -------------------------------

def compute_fcr(gt, pred):
    correct = 0
    total = 0

    for f in REQUIRED_FIELDS:
        if field_exists(f, gt):
            total += 1
            if f in pred and normalize(gt[f]) == normalize(pred[f]):
                correct += 1

    return correct / total if total > 0 else 0


# -------------------------------
# SPS: Schema Precision Score
# Penalises predictions that include unexpected extra keys
# -------------------------------

def compute_sps(pred):
    pred_fields = set(pred.keys())
    known_fields = set(REQUIRED_FIELDS) | set(OPTIONAL_FIELDS)
    required_fields = set(REQUIRED_FIELDS)

    correct_fields = pred_fields & required_fields
    extra_fields = pred_fields - known_fields   # truly unexpected fields

    if not pred_fields:
        return 0

    return len(correct_fields) / (len(correct_fields) + len(extra_fields))


# -------------------------------
# OSC: Optional Style Coverage
# Measures how many optional style fields were captured
# (purely informational — not averaged into final score)
# -------------------------------

def compute_osc(pred):
    if not OPTIONAL_FIELDS:
        return 1.0
    present = sum(1 for f in OPTIONAL_FIELDS if field_exists(f, pred))
    return present / len(OPTIONAL_FIELDS)


# -------------------------------
# MAIN EVALUATION
# -------------------------------

def evaluate(dataset):
    total_fcs = 0
    total_fcr = 0
    total_sps = 0
    total_osc = 0

    n = len(dataset)

    for sample in dataset:
        gt   = sample["ground_truth"]
        pred = sample["prediction"]

        fcs = compute_fcs(gt, pred)
        fcr = compute_fcr(gt, pred)
        sps = compute_sps(pred)
        osc = compute_osc(pred)

        total_fcs += fcs
        total_fcr += fcr
        total_sps += sps
        total_osc += osc

    print("----- FINAL SCORES -----")
    print(f"FCS (Field Coverage Score):      {total_fcs / n:.4f}")
    print(f"FCR (Field Correctness Rate):    {total_fcr / n:.4f}")
    print(f"SPS (Schema Precision Score):    {total_sps / n:.4f}")
    print(f"OSC (Optional Style Coverage):   {total_osc / n:.4f}  [informational]")


# -------------------------------
# LOAD DATASET
# -------------------------------

if __name__ == "__main__":
    with open("dataset_with_predictions.json", "r") as f:
        data = json.load(f)

    evaluate(data)