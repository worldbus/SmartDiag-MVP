# ai_analyzer.py

import os
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

from openai import OpenAI

def analyze_results(domain: str, ping_trace: str, speed: dict) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "**AI Analysis unavailable: no API key set.**"

    client = OpenAI(api_key=api_key)

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
        if "insufficient_quota" in err:
            return "🔍 AI Analysis currently unavailable (quota)."
        if "Invalid API Key" in err:
            return "**AI Analysis unavailable: invalid API key.**"
        return f"**AI Analysis error:** {err}"
