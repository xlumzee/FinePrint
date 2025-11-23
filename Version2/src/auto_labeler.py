# rule based clause labeling - weak supervision

from clause_splitter import split_into_clauses
from risk_detector import detect_risk

def auto_label_clauses(text):
    """
    Takes full policy text, splits into clauses and assigns labels.
    returns list of dicts with clause and label
    """
    clauses = split_into_clauses(text)
    labeled = []

    for clause in clauses:
        # detect risk in just a single clause
        risks = detect_risk(clause)

        if len(risks) == 0:
            # no rule matched basically
            labeled.append({
                "clause": clause,
                "label": "none"
            })
        else:
            # one label for each match
            # if multiple match, for now - 1st one, need to fix this later
            main_label = list(risks.keys())[0]

            labeled.append({
                "clause": clause,
                "label": main_label
            })

    return labeled