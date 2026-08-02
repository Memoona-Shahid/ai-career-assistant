from datetime import datetime

from config import client, MODEL_NAME
from constants import Command, MAX_HISTORY
from logger import logger, save_history
from models import ChatSession
from utils import (
    export_chat,
    load_chat_json,
    save_chat_json,
    timestamp,
)


class CareerAssistant:
    """
    AI Career Assistant that interacts with Gemini,
    manages chat history, and handles user commands.
    """

    def __init__(self) -> None:
        """
        Initialize the assistant.
        """

        history: list = load_chat_json()

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
        """
        Generate a response from Gemini AI.
        """

        logger.info(f"User asked: {question}")

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=f"""
You are an experienced AI Career Coach.

Question:
{question}
""",
        )

        answer: str = response.text

        logger.info("Response generated successfully.")

        self.session.history.append(
            {
                "question": question,
                "answer": answer,
            }
        )

        # Keep only the latest MAX_HISTORY conversations
        if len(self.session.history) > MAX_HISTORY:
            self.session.history.pop(0)
            logger.info(
                f"History limit exceeded. Oldest conversation removed. Maximum history: {MAX_HISTORY}"
            )

        self.session.question_count += 1

        save_history(question, answer)

        return answer

    def show_history(self) -> None:
        """
        Display previous conversations.
        """

        if not self.session.history:
            logger.warning("History requested but no history found.")
            print("No history found.")
            return

        logger.info("Conversation history viewed.")

        print("\nConversation History")
        print("-" * 50)

        for index, chat in enumerate(self.session.history, start=1):
            print(f"\nQ{index}: {chat['question']}")
            print(f"A{index}: {chat['answer']}")

    def clear_history(self) -> None:
        """
        Clear chat history.
        """

        self.session.history.clear()

        logger.info("Conversation history cleared.")

        print("History cleared.")

    def print_summary(self) -> None:
        """
        Display today's session summary.
        """

        end_time = datetime.now()

        session_time = end_time - self.session.created_at

        minutes = session_time.seconds // 60
        seconds = session_time.seconds % 60

        print("\n" + "=" * 40)
        print("Today's Session")
        print("=" * 40)
        print(f"Questions Asked : {self.session.question_count}")
        print(f"Session Length  : {minutes} min {seconds} sec")
        print("=" * 40)

    def start_chat(self) -> None:
        """
        Start the interactive chat session.
        """

        logger.info("Application started.")

        while True:

            question: str = input("\nYou: ").strip()

            if not question:
                logger.warning("User entered an empty question.")
                print("Please enter a question.")
                continue

            command = question.lower()

            if command == Command.EXIT.value:

                logger.info("Application closed.")

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

                logger.info("Help menu opened.")

                print("""
========================================
        Available Commands
========================================

/help      Show this menu

/history   View conversation history

/clear     Clear current session

/save      Save chat history

/exit      Exit application

/export    Export conversation (.md)

========================================
""")
                continue

            elif command == Command.SAVE.value:

                try:
                    save_chat_json(self.session.history)

                    logger.info("Chat history saved successfully.")

                    print("✅ Chat saved successfully.")

                except Exception:
                    logger.exception("Failed to save chat history.")

                    print("Unable to save chat history.")

                continue
            elif command == Command.EXPORT.value:

                try:
                    export_path = export_chat(self.session.history)

                    logger.info(f"Chat exported successfully to {export_path}.")

                    print(f"✅ Chat exported successfully to {export_path}.")

                except Exception:
                    logger.exception("Failed to export chat history.")

                    print("Unable to export chat history.")

                continue

            try:

                answer = self.generate_response(question)

                print(f"\n[{timestamp()}]")
                print(f"Assistant: {answer}")

            except Exception:
                logger.exception("Failed to generate AI response.")

                print("\nSomething went wrong while contacting Gemini.")
                print("Please try again.")