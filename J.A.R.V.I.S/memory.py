import json

from pathlib import Path


MEMORY_FILE = Path(__file__).parent / "jarvis_memory.json"


def load_memory():

    if MEMORY_FILE.exists():

        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    return []


def save_memory(history):

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            history,
            file,
            indent=4
        )


def add_memory(history, user_message, ai_response):

    history.append({

        "role": "user",

        "content": user_message

    })

    history.append({

        "role": "assistant",

        "content": ai_response

    })

    save_memory(history)

    return history