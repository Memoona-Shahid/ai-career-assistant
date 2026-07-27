from datetime import datetime


def save_history(question, answer):
    with open("history.txt", "a", encoding="utf-8") as file:
        file.write(f"\n[{datetime.now()}]\n")
        file.write(f"You: {question}\n")
        file.write(f"Assistant: {answer}\n")
        file.write("-" * 50 + "\n")