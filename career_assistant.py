from datetime import datetime

from config import client, MODEL_NAME
from logger import logger, save_history
from utils import (
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
        self.history: list = load_chat_json()

        if self.history:
            logger.info(f"Loaded {len(self.history)} previous conversations.")
            print(f"Loaded {len(self.history)} previous conversations.")

        self.question_count: int = 0
        self.start_time: datetime = datetime.now()

    def generate_response(self, question: str) -> str:
        """
        Generate a response from Gemini AI.

        Args:
            question: User's question.

        Returns:
            AI-generated response.
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

        self.history.append(
            {
                "question": question,
                "answer": answer,
            }
        )

        self.question_count += 1

        save_history(question, answer)

        return answer

    def show_history(self) -> None:
        """
        Display previous conversations.
        """

        if not self.history:
            logger.warning("History requested but no history found.")
            print("No history found.")
            return

        logger.info("Conversation history viewed.")

        print("\nConversation History")
        print("-" * 50)

        for index, chat in enumerate(self.history, start=1):
            print(f"\nQ{index}: {chat['question']}")
            print(f"A{index}: {chat['answer']}")

    def clear_history(self) -> None:
        """
        Clear chat history.
        """

        self.history.clear()

        logger.info("Conversation history cleared.")

        print("History cleared.")

    def print_summary(self) -> None:
        """
        Display today's session summary.
        """

        end_time = datetime.now()

        session_time = end_time - self.start_time

        minutes = session_time.seconds // 60
        seconds = session_time.seconds % 60

        print("\n" + "=" * 40)
        print("Today's Session")
        print("=" * 40)
        print(f"Questions Asked : {self.question_count}")
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

            if command == "/exit":

                logger.info("Application closed.")

                self.print_summary()

                print("\nGoodbye!")

                break

            elif command == "/history":

                self.show_history()
                continue

            elif command == "/clear":

                self.clear_history()
                continue

            elif command == "/help":

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

========================================
""")
                continue

            elif command == "/save":

                try:
                    save_chat_json(self.history)

                    logger.info("Chat history saved successfully.")

                    print("✅ Chat saved successfully.")

                except Exception:
                    logger.exception("Failed to save chat history.")

                    print("Unable to save chat history.")

                continue

            try:

                answer = self.generate_response(question)

                print(f"\n[{timestamp()}]")
                print(f"Assistant: {answer}")

            except Exception:
                logger.exception("Failed to generate AI response.")

                print("\nSomething went wrong while contacting Gemini.")
                print("Please try again.")