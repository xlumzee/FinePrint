# Rule based clause detection

import re

# Simple keyword patterns

RISK_PATTERNS = {
    "data_sharing": [
        r"share your data",
        r"share information",
        r"third[- ]party",
        r"sell your data",
        r"data brokers"
    ],
    "tracking": [
        r"cookies",
        r"track",
        r"tracking technologies",
        r"collect usage data",
        r"device identifiers"
    ],
    "location": [
        r"location data",
        r"geo[- ]location",
        r"precise location"
    ],
    "ai_decisions": [
        r"automated decision",
        r"algorithmic decision",
        r"profiling",
        r"ai[- ]based"
    ],
    "refunds": [
        r"non[- ]refundable",
        r"refund",
        r"cancellation fee",
        r"no refunds"
    ],
    "employment_checks": [
        r"background check",
        r"employment verification",
        r"criminal history"
    ],
    "arbitration": [
        r"binding arbitration",
        r"waive your right",
        r"class action",
        r"dispute resolution"
    ],
    "auto_renewal": [
        r"auto[- ]renew",
        r"automatically renew",
        r"recurring charges"
    ],

}

def detect_risk(text):
    """
    Returns a dict of detected risk categories with the exact clauses/snippets that triggered detection.
    """

    detected = {}

    for category, patterns in RISK_PATTERNS.items():
        matches = []

        for pattern in patterns:
            regex = re.compile(pattern, re.IGNORECASE)
            found = regex.findall(text)

            if found:
                #extract snippet around each match
                lines = text.split("\n")
                for line in lines:
                    if re.search(pattern, line, re.IGNORECASE):
                        matches.append(line.strip())

        if matches:
            detected[category] = matches
        
    return detected