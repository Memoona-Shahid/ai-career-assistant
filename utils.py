from datetime import datetime
from pathlib import Path
import json

from config import HISTORY_DIR, EXPORT_DIR


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
    """

    return datetime.now().strftime("%I:%M %p")


def load_chat_json() -> list:
    """
    Load the latest chat history.
    """

    history_path = Path(HISTORY_DIR)

    history_path.mkdir(parents=True, exist_ok=True)

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
    Save chat history as a JSON session.
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


def export_chat(history: list) -> Path:
    """
    Export the current conversation to a Markdown file.

    Args:
        history: Conversation history.

    Returns:
        Path of the exported Markdown file.
    """

    export_path = Path(EXPORT_DIR)

    export_path.mkdir(parents=True, exist_ok=True)

    filename = (
        export_path
        / f"chat_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.md"
    )

    lines = [
        "# AI Career Assistant Session",
        "",
        f"Exported: {datetime.now().strftime('%d %B %Y %I:%M %p')}",
        "",
    ]

    for chat in history:

        lines.append("## User")
        lines.append(chat["question"])
        lines.append("")

        lines.append("## Assistant")
        lines.append(chat["answer"])
        lines.append("")
        lines.append("---")
        lines.append("")

    filename.write_text("\n".join(lines), encoding="utf-8")

    return filename