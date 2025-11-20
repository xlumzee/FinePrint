# summarizer.py — upgraded summarizer with chunking support

import os
from dotenv import load_dotenv
from openai import OpenAI
from chunker import chunk_text

load_dotenv()  # load variables from .env

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_chunk(text):
    """Summarize a single chunk of text."""
    prompt = f"""
    Summarize the following text into 3–5 simple bullet points.
    Make it extremely easy to understand.

    Text:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def summarize_policy(text):
    """Summarize an entire policy (short or long) with automatic chunking."""

    # 1. If text is short enough → summarize directly
    if len(text) < 3000:
        return summarize_chunk(text)

    # 2. If long → chunk it
    chunks = chunk_text(text, max_chars=3000)

    # 3. Summarize each chunk
    chunk_summaries = []
    for idx, chunk in enumerate(chunks):
        summary = summarize_chunk(chunk)
        chunk_summaries.append(f"Chunk {idx+1} Summary:\n{summary}")

    combined_text = "\n\n".join(chunk_summaries)

    # 4. Final combined summary
    final_prompt = f"""
    Combine the following chunk summaries into a single, clean 5‑bullet summary.
    Remove repetition and keep it extremely clear.

    {combined_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": final_prompt}]
    )

    return response.choices[0].message.content