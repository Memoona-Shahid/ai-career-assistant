from datetime import datetime

from config import client, MODEL_NAME
from constants import Command, MAX_HISTORY
from logger import logger, save_history
from models import ChatSession
from utils import (
    export_chat,
    load_chat_json,
    print_header,
    save_chat_json,
    search_history,
    timestamp,
)


class CareerAssistant:
    """
    AI Career Assistant that interacts with Gemini,
    manages chat history, and handles user commands.
    """

    def __init__(self) -> None:

        history = load_chat_json()

        if history:
            logger.info(f"Loaded {len(history)} previous conversations.")
            print(f"Loaded {len(history)} previous conversations.")

        self.session = ChatSession(
            session_id=datetime.now().strftime("%Y%m%d_%H%M%S"),
            created_at=datetime.now(),
            question_count=0,
            history=history,
        )

    def generate_response(self, question: str) -> str:

        logger.info(f"User asked: {question}")

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=f"""
You are an experienced AI Career Coach.

Question:
{question}
""",
        )

        answer = response.text

        logger.info("Response generated successfully.")

        self.session.history.append(
            {
                "question": question,
                "answer": answer,
            }
        )

        if len(self.session.history) > MAX_HISTORY:
            self.session.history.pop(0)
            logger.info("Oldest conversation removed.")

        self.session.question_count += 1

        save_history(question, answer)

        return answer

    def show_history(self) -> None:

        if not self.session.history:
            print("No history found.")
            return

        print_header("Conversation History")

        for index, chat in enumerate(self.session.history, start=1):
            print(f"\nQ{index}: {chat['question']}")
            print(f"A{index}: {chat['answer']}")

    def clear_history(self) -> None:

        self.session.history.clear()

        logger.info("Conversation history cleared.")

        print("History cleared.")

    def print_summary(self) -> None:

        end_time = datetime.now()

        session_time = end_time - self.session.created_at

        minutes = session_time.seconds // 60
        seconds = session_time.seconds % 60

        print_header("Today's Session", 40)

        print(f"Questions Asked : {self.session.question_count}")
        print(f"Session Length  : {minutes} min {seconds} sec")

    def start_chat(self) -> None:

        logger.info("Application started.")

        while True:

            question = input("\nYou: ").strip()

            if not question:
                print("Please enter a question.")
                continue

            command = question.lower()

            if command == Command.EXIT.value:

                self.print_summary()

                print("\nGoodbye!")

                break

            elif command == Command.HISTORY.value:

                self.show_history()
                continue

            elif command == Command.CLEAR.value:

                self.clear_history()
                continue

            elif command == Command.HELP.value:

                print("""
========================================
Available Commands
========================================

/help
/history
/clear
/save
/export
/search <keyword>
/exit

========================================
""")
                continue

            elif command == Command.SAVE.value:

                save_chat_json(self.session.history)

                print("Chat saved successfully.")

                continue

            elif command == Command.EXPORT.value:

                export_path = export_chat(self.session.history)

                print(f"Exported to:\n{export_path}")

                continue

            elif command.startswith("/search"):

                parts = question.split(maxsplit=1)

                if len(parts) < 2:

                    print("Usage: /search <keyword>")

                    continue

                keyword = parts[1]

                results = search_history(self.session.history, keyword)

                if not results:

                    print("\nNo matching conversations found.")

                    continue

                print_header("Search Results")

                for index, chat in enumerate(results, start=1):

                    print(f"\nResult {index}")
                    print(f"Question: {chat['question']}")
                    print(f"Answer: {chat['answer']}")
                    print("-" * 50)

                continue

            try:

                answer = self.generate_response(question)

                print(f"\n[{timestamp()}]")
                print(f"Assistant: {answer}")

            except Exception as e:

                logger.exception(e)

                print("Something went wrong.")