# label mapping for classifier

LABELS = [
    "none",
    "data_sharing",
    "tracking",
    "refunds",
    "location",
    "arbitration",
    "ai_decisions",
]

label2id = {label: i for i, label in enumerate(LABELS)}
id2label = {i: label for label, i in label2id.items()}