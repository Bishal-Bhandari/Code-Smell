import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def review_with_llm(code: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a senior software engineer reviewing code."},
                {"role": "user", "content": f"Review this code and suggest improvements:\n{code}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return str(e)