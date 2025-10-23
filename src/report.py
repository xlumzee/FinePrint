from pathlib import Path

def write_markdown(out_path, title, general, pitfalls, benefits):
    md = [f"# Privacy Summary — {title}", ""]
    md += ["## General TL;DR"] + [f"- {s}" for s in general] + [""]
    md += ["## Pitfalls (Risks)"] + [f"- {s}" for s in pitfalls] + [""]
    md += ["## Benefits (Safeguards)"] + [f"- {s}" for s in benefits] + [""]
    Path(out_path).write_text("\n".join(md), encoding="utf-8")