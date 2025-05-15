# ai_analyzer.py

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_results(domain: str, ping_trace: str, speed: dict) -> str:
    prompt = (
        f"Domain: {domain}\n\n"
        f"{ping_trace}\n\n"
        f"Speed test: {speed}\n\n"
        "Please summarize these results in plain English."
    )
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        err = str(e)
        if "RateLimitError" in err:
            return "**AI Analysis temporarily unavailable (rate limit).**"
        if "AuthenticationError" in err or "Invalid API Key" in err:
            return "**AI Analysis unavailable: invalid API key.**"
        return f"**AI Analysis error:** {err}"
