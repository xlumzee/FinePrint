# improved rule-based clause classification

import re

# better risk patterns

RISK_PATTERNS = {
    "data_sharing": [
        r"share your data",
        r"share information",
        r"we share",
        r"we may share",
        r"sharing with",
        r"we disclose",
        r"we may disclose",
        r"disclose your",
        r"third[- ]?party",
        r"third[- ]?parties",
        r"service providers",
        r"analytics partners",
        r"business partners",
        r"sell your data",
        r"data brokers",
        r"provide.*?to third",
        r"transfer.*?data"
    ],

    "tracking": [
        r"cookies?",
        r"cookie policy",
        r"tracking technologies",
        r"track(?:ing)?",
        r"device identifiers",
        r"pixel tags",
        r"web beacons",
        r"collect usage data",
        r"usage analytics",
        r"online activity",
        r"advertising identifier",
        r"ip address"
    ],

    "location": [
        r"location data",
        r"precise location",
        r"approximate location",
        r"geo[- ]?location",
        r"geolocation",
        r"gps",
        r"location services"
    ],

    "ai_decisions": [
        r"automated decision",
        r"automated processing",
        r"algorithmic decision",
        r"algorithmic processing",
        r"profiling",
        r"ai[- ]?based",
        r"machine learning",
        r"automated.*(screening|evaluation)",
        r"automated.*(hiring|employment)",
        r"model[- ]?based",
        r"predictive analytics",
        r"automated moderation",
        r"automated recommendations"
    ],

    "refunds": [
        r"refund",
        r"refunds policy",
        r"non[- ]refundable",
        r"no refunds",
        r"cancellation fee",
        r"no cancellation",
        r"not eligible for refund"
    ],

    "employment_checks": [
        r"background check",
        r"criminal history",
        r"employment verification",
        r"identity verification",
        r"right to work",
        r"work eligibility",
        r"pre[- ]?employment screening"
    ],

    "arbitration": [
        r"binding arbitration",
        r"arbitration agreement",
        r"waive your right",
        r"waiver of rights",
        r"no class action",
        r"class action waiver",
        r"dispute resolution",
        r"resolve.*?arbitration"
    ],

    "auto_renewal": [
        r"auto[- ]renew",
        r"automatic renewal",
        r"automatically renew",
        r"recurring charges",
        r"subscription renews",
        r"renewal terms"
    ]
}



def detect_risk(text):
    """
    Improved risk detection:
    - scans entire clause
    - expanded keyword coverage
    - scoring per category
    - returns BEST matching category only
    """

    category_scores = {cat: 0 for cat in RISK_PATTERNS}
    matches_by_category = {cat: [] for cat in RISK_PATTERNS}

    # Scan clause (NOT entire policy lines)
    for category, patterns in RISK_PATTERNS.items():
        for pattern in patterns:
            regex = re.compile(pattern, re.IGNORECASE)
            found = regex.findall(text)

            if found:
                category_scores[category] += len(found)
                matches_by_category[category].extend(found)

    # Choose the best-scoring category
    best_category = None
    best_score = 0

    for category, score in category_scores.items():
        if score > best_score:
            best_score = score
            best_category = category

    # No matches at all
    if best_score == 0 or best_category is None:
        return {}

    # Return category with the strongest evidence
    return {best_category: matches_by_category[best_category]}