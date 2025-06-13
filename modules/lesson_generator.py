import requests
import os

TOGETHER_API_KEY = os.getenv("c60ae9468c290bda303a18c78f228466a5d70488e790e6019b81cdb1bdac1bbd")
TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"

def generate_lesson(topic, level="Beginner", style="Summary"):
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/Mistral-7B-Instruct-v0.2",  # or another model from Together
        "messages": [
            {"role": "system", "content": "You are a helpful educational assistant."},
            {"role": "user", "content": f"Create a {style.lower()} style lesson on '{topic}' for a {level.lower()} learner."}
        ],
        "temperature": 0.7,
        "max_tokens": 800
    }

    try:
        response = requests.post(TOGETHER_API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"⚠️ Error generating lesson: {e}"
