import json
import os
from datetime import datetime

def welcome():
    now = datetime.now()

    print("=" * 50)
    print("🤖 AI Career Assistant")
    print("=" * 50)
    print("Welcome Memoona!")
    print(f"Today's Date    : {now.strftime('%d %B %Y')}")
    print(f"Session Started : {now.strftime('%I:%M %p')}")
    print("=" * 50)
def timestamp():
    return datetime.now().strftime("%I:%M %p")

def load_chat_json():

    if not os.path.exists("chat_history.json"):
        return []

    with open("chat_history.json", "r", encoding="utf-8") as file:
        return json.load(file) 
    
def save_chat_json(history):
    with open("chat_history.json", "w", encoding="utf-8") as file:
        json.dump(
            history,
            file,
            indent=4,
            ensure_ascii=False
        )