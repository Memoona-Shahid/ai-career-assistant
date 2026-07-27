from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    filename="assistant.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


def save_history(question, answer):
    with open("history.txt", "a", encoding="utf-8") as file:
        file.write(f"\n[{datetime.now()}]\n")
        file.write(f"You: {question}\n")
        file.write(f"Assistant: {answer}\n")
        file.write("-" * 50 + "\n")