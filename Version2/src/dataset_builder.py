import csv
import os
from extractor import load_policy, clean_text
from auto_labeler import auto_label_clauses

def build_dataset(policy_path, output_path, source_name="unknown"):
    """
    Takes a privacy policy text file, auto labels clauses,, and saves dataset to CSV. 
    """

    raw = load_policy(policy_path)

    cleaned = clean_text(raw)

    labeled = auto_label_clauses(cleaned)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["clause", "label", "source_policy"])

        for item in labeled:
            writer.writerow([item["clause"], item["label"], source_name])

    print(f"Dataset saved to {output_path} with {len(labeled)} rows. ")