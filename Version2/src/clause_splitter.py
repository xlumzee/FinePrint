# split long policy text into individual clauses/sentences

import re

def split_into_clauses(text):
    """
    Splits policy text into sentence-like clauses.
    Uses punctuation and line breaks as boundaries.
    """

    # normalize spacing
    text = text.replace("\n", " ").strip()

    # split based on ., ?, ! but keep the delimiter
    raw_clauses = re.split(r'(?<=[.!?])\s+', text)

    clauses = []

    for clause in raw_clauses:
        cleaned = clause.strip()

        #skipping very short fragments
        if len(cleaned) < 40:
            continue

        # skipping weird broken lines or titles
        if cleaned.count(" ") < 3:
            continue

        clauses.append(cleaned)
    
    return clauses