from pathlib import Path
from src.io_utils import read_text, write_jsonl
from src.preprocess import normalize, to_sentences, doc_id_from_path
from src.rules import label_sentence
from src.summarize import mmr
from src.report import write_markdown

RAW = "data/raw/doc_0001.html"   # change to your file
title = Path(RAW).name

def main():
    raw = read_text(RAW)
    text = normalize(raw)
    sents = [(i, s) for i, s in to_sentences(text)]
    rows = []
    for sid, s in sents:
        lab, rules = label_sentence(s)
        rows.append({"sent_id": sid, "text": s, "label": lab, "rules": rules})
    write_jsonl("data/processed/doc_0001.jsonl", rows)

    # General summary via MMR
    general = mmr([r["text"] for r in rows], k=6)

    # Pick top risk/safe by simple scoring: count rule hits + length penalty
    def top_by(label, k=5):
        cand = [r for r in rows if r["label"]==label]
        cand = sorted(cand, key=lambda r: (len(r["rules"]), len(r["text"])/200), reverse=True)
        return mmr([c["text"] for c in cand][:20], k=min(k, len(cand))) if cand else []

    pitfalls = top_by("risk", k=5)
    benefits = top_by("safe", k=5)

    write_markdown("reports/doc_0001_summary.md", title, general, pitfalls, benefits)
    print("✅ Wrote: reports/doc_0001_summary.md")
    print("   Sentences processed:", len(rows))
    print("   Risk/Safe counts:", sum(r['label']=='risk' for r in rows), "/", sum(r['label']=='safe' for r in rows))

if __name__ == "__main__":
    main()