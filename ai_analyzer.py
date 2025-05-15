# ai_analyzer.py

import os
from openai import OpenAI

# instantiate the new client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_results(domain: str, ping_trace: str, speed: dict) -> str:
    prompt = (
        f"Domain: {domain}\n\n"
        f"{ping_trace}\n\n"
        f"Speed test: {speed}\n\n"
        "Please summarize these results in plain English."
    )
    # use the new chat.completions endpoint
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    # new API returns message under .choices[0].message.content
    return response.choices[0].message.content.strip()
