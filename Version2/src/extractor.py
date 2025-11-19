def load_policy(path):
    """Load raw policy text from a file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    
def clean_text(text):
    """Basic cleanup. Removes empty lines, normalizes spaces"""
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return "\n".join(lines)