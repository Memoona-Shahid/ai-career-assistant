from datetime import datetime


def banner():
    print("=" * 50)
    print("AI Career Assistant")
    print("Powered by Gemini")
    print("=" * 50)


def timestamp():
    return datetime.now().strftime("%I:%M %p")