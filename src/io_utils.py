from pathlib import Path
import json

def write_jsonl(path, rows):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

def read_text(path):
    p = Path(path)
    if p.suffix.lower() == ".txt":
        return p.read_text(encoding="utf-8", errors="ignore")
    if p.suffix.lower() in {".html", ".htm"}:
        import trafilatura
        raw = p.read_text(encoding="utf-8", errors="ignore")
        out = trafilatura.extract(raw, include_links=False, include_tables=False) or raw
        return out
    if p.suffix.lower() == ".pdf":
        from pypdf import PdfReader
        txt = []
        for page in PdfReader(str(p)).pages:
            txt.append(page.extract_text() or "")
        return "\n".join(txt)
    raise ValueError(f"Unsupported file type: {p.suffix}")