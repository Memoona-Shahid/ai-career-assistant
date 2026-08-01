from datetime import datetime
from pathlib import Path
import json

from config import HISTORY_DIR


def welcome() -> None:
    """
    Display the application welcome screen.
    """

    now = datetime.now()

    print("=" * 50)
    print("🤖 AI Career Assistant")
    print("=" * 50)
    print("Welcome Memoona!")
    print(f"Today's Date    : {now.strftime('%d %B %Y')}")
    print(f"Session Started : {now.strftime('%I:%M %p')}")
    print("=" * 50)


def timestamp() -> str:
    """
    Return the current time.

    Returns:
        Current time formatted as HH:MM AM/PM.
    """

    return datetime.now().strftime("%I:%M %p")


def load_chat_json() -> list:
    """
    Load the most recent chat history.

    Returns:
        List containing previous conversation.
        Returns an empty list if no history exists.
    """

    history_path = Path(HISTORY_DIR)

    if not history_path.exists():
        history_path.mkdir(parents=True)

    files = sorted(history_path.glob("session_*.json"))

    if not files:
        return []

    latest_file = files[-1]

    try:
        return json.loads(latest_file.read_text(encoding="utf-8"))

    except json.JSONDecodeError:
        return []


def save_chat_json(history: list) -> None:
    """
    Save the current conversation into a new session file.

    Args:
        history: Conversation history.
    """

    history_path = Path(HISTORY_DIR)

    history_path.mkdir(parents=True, exist_ok=True)

    filename = (
        history_path
        / f"session_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
    )

    filename.write_text(
        json.dumps(
            history,
            indent=4,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )