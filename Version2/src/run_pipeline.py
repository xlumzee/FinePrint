#looks at all files in raw, regardless of name and runs the pipeline, generates individual laveled csvs and produces a merged master file

import os
import glob
import pandas as pd

from dataset_builder import build_dataset

RAW_DIR = "../data/raw/"
PROCESSED_DIR = "../data/processed/"

def run_pipeline():
    # need to get all txt files
    files = glob.glob(os.path.join(RAW_DIR, "*.txt"))
    print(f"Found {len(files)} raw policy files. \n")

    csv_files = []

    # run build dataset on each file
    for f in files:
        name = os.path.basename(f).replace(".txt", "")
        output_csv = os.path.join(PROCESSED_DIR, f"{name}_clauses_labeled.csv")

        print(f"processing: {name}...")
        build_dataset(f, output_csv, source_name=name)
        csv_files.append(output_csv)

    # merging all csvs
    dfs = [pd.read_csv(csv) for csv in csv_files]
    combined = pd.concat(dfs, ignore_index=True)

    combined_path = os.path.join(PROCESSED_DIR, "all_clauses_raw.csv")
    combined.to_csv(combined_path, index=False)
    print(f"\nMerged datset saved to {combined_path}")

    return combined
