# this should use an LLM to produce a simple 5 bullet summary

from openai import OpenAI
client = OpenAI()

def summarize_policy(text):
    prompt = f"""
    Summarize the following privacy policy into 5 simple bullet points.
    Keep it very easy to understand.

    Policy text:
    {text}
    """
    response = client.chat.completions.create(model = "gpt-4o-mini", messages = [{"role": "user", "content": prompt}])
    return response.choices[0].message["content"]