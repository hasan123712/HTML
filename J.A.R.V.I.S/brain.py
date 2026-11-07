import requests

MODEL = "qwen2.5:3b"

API = "http://localhost:11434/api/chat"


def ask_ai(question, history=None):

    if history is None:
        history = []

    messages = [
        {
            "role": "system",
            "content": """
            You are JARVIS, an intelligent AI assistant.

            You help with:
            - Research
            - Programming
            - Productivity
            - Computer tasks
            - Learning

            Be intelligent, helpful and professional.

            Never claim to have completed an action
            unless it was actually completed.
            """
        }
    ]

    messages.extend(history[-12:])

    messages.append({
        "role": "user",
        "content": question
    })

    data = {
        "model": MODEL,
        "messages": messages,
        "stream": False
    }

    response = requests.post(
        API,
        json=data,
        timeout=180
    )

    response.raise_for_status()

    result = response.json()

    return result["message"]["content"]