# this should use an LLM to produce a simple 5 bullet summary

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() # load variables from .env

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_policy(text):
    prompt = f"""
    Summarize the following privacy policy into 5 simple bullet points.
    Keep it very easy to understand.

    Policy text:
    {text}
    """
    response = client.chat.completions.create(model = "gpt-4o-mini", messages = [{"role": "user", "content": prompt}])
    return response.choices[0].message["content"]