# ai_analyzer.py

import os
from openai import OpenAI, error

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
    except error.RateLimitError:
        return "**AI Analysis temporarily unavailable (rate limit). Please try again later.**"
    except error.AuthenticationError:
        return "**AI Analysis unavailable: invalid API key.**"
    except Exception as e:
        return f"**AI Analysis error:** {e}"
