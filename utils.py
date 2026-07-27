import json
from datetime import datetime


def banner():
    print("=" * 50)
    print("AI Career Assistant")
    print("Powered by Gemini")
    print("=" * 50)


def timestamp():
    return datetime.now().strftime("%I:%M %p")


def save_chat_json(history):
    with open("chat_history.json", "w", encoding="utf-8") as file:
        json.dump(
            history,
            file,
            indent=4,
            ensure_ascii=False
        )