# weak labels for pitfalls/benefits

import re
Rule = tuple[str, str, "re.Pattern"]

PITFALLS: list[Rule] = [
    ("sell_data","risk", re.compile(r"(sell|sale|monetiz\w+).*\b(data|information)\b", re.I)),
    ("third_party","risk", re.compile(r"(share|disclos\w+|provide).*\b(third[- ]?part|affiliate|partner)s?\b", re.I)),
    ("tracking","risk", re.compile(r"(track|profile|ad[s ]?tech|cookie|pixel|beacon).*\b(across|other sites|third)", re.I)),
    ("sensitive","risk", re.compile(r"(biometric|precise location|health|genetic|ssn|social security|financial account)", re.I)),
    ("retention_long","risk", re.compile(r"(retain|storage).*(indefinite|as long as necessary|permanent|extended)", re.I)),
    ("arbitration","risk", re.compile(r"(arbitration|class action (waiver|release)|binding dispute)", re.I)),
    ("sale_merger","risk", re.compile(r"(merger|acquisition|bankruptcy|asset sale).*\b(data|information)\b", re.I)),
]

BENEFITS: list[Rule] = [
    ("no_sale","safe", re.compile(r"(do not|never).*\b(sell)\b.*\b(data|information)\b", re.I)),
    ("data_min","safe", re.compile(r"(collect (only|just)|data minimization|minim(um|ize) necessary)", re.I)),
    ("encryption","safe", re.compile(r"(encrypt(ed|ion)|at rest|in transit)", re.I)),
    ("user_controls","safe", re.compile(r"(opt-?out|opt-?in|preferences|do not sell|delete my data|access request)", re.I)),
    ("retention_limits","safe", re.compile(r"(retain|delete).*(short|limited|fixed (period|time))", re.I)),
    ("privacy_contact","safe", re.compile(r"(data protection officer|privacy@|privacy office|gdpr contact)", re.I)),
]

INFO: list[Rule] = [
    ("law","info", re.compile(r"(law enforcement|subpoena|court order|legal request)", re.I)),
    ("processors","info", re.compile(r"(processor|vendor|sub[- ]?processor|service provider)", re.I)),
    ("intl","info", re.compile(r"(transfer|store).*\b(EU|EEA|UK|US|international|cross[- ]?border)\b", re.I)),
]

ALL = PITFALLS + BENEFITS + INFO
PRIORITY = {"risk":3, "safe":2, "info":1, "neutral":0}

def label_sentence(s:str):
    hits = [(rid, typ) for rid, typ, rx in ALL if rx.search(s)]
    if not hits:
        return "neutral", []
    # choose dominant by priority; keep all hit ids for debugging
    dominant = sorted(hits, key=lambda x: PRIORITY[x[1]], reverse=True)[0][1]
    return dominant, [h[0] for h in hits]