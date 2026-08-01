from datetime import datetime
from logging.handlers import RotatingFileHandler
from pathlib import Path
import logging

from config import LOG_DIR


# ======================================================
# Configure Logger
# ======================================================

LOG_FILE = LOG_DIR / "assistant.log"

logger = logging.getLogger("career_assistant")
logger.setLevel(logging.INFO)

if not logger.handlers:

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=1_000_000,   # 1 MB
        backupCount=5,
        encoding="utf-8",
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)


# ======================================================
# Save Conversation
# ======================================================

def save_history(question: str, answer: str) -> None:
    """
    Save a conversation to a text file.

    Args:
        question: User's question.
        answer: AI-generated answer.
    """

    history_file = Path("history") / "conversation.txt"

    with history_file.open(
        "a",
        encoding="utf-8",
    ) as file:

        file.write(f"\n[{datetime.now()}]\n")
        file.write(f"You: {question}\n")
        file.write(f"Assistant: {answer}\n")
        file.write("-" * 60 + "\n")