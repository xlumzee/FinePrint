# this file will split long policy into manageable chunks

def chunk_text(text, max_chars= 3000):
    """
    Split text into chunks of max_chars length.
    Keeps chunks aligned to paragraph boundaries when possible.
    """
    paragraphs = text.split("\n")
    chunks = []
    current_chunk = ""

    for p in paragraphs:
        if len(current_chunk) + len(p) < max_chars:
            current_chunk += p + "\n"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = p + "\n"
        
    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks