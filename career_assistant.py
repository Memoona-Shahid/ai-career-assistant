from datetime import datetime
from utils import load_chat_json
from config import client
from logger import logger, save_history
from utils import timestamp, save_chat_json


class CareerAssistant:

    def __init__(self):
        self.history = load_chat_json()

        if self.history:
            print(f"Loaded {len(self.history)} previous conversations.")
        self.question_count = 0
        self.start_time = datetime.now()

    def generate_response(self, question):

        logger.info(f"User asked: {question}")

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=f"""
You are an experienced AI Career Coach.

Question:
{question}
"""
        )

        answer = response.text

        logger.info("Response generated successfully")

        self.history.append({
            "question": question,
            "answer": answer
        })

        self.question_count += 1

        save_history(question, answer)

        return answer

    def show_history(self):

        if not self.history:
            print("No history found.")
            return

        logger.info("Conversation history viewed")

        print("\nConversation History")
        print("-" * 40)

        for i, chat in enumerate(self.history, start=1):
            print(f"\nQ{i}: {chat['question']}")
            print(f"A{i}: {chat['answer']}")

    def clear_history(self):

        self.history.clear()

        logger.info("Conversation history cleared")

        print("History cleared.")

    def start_chat(self):

        while True:

            question = input("\nYou: ")

            if question.lower() == "/exit":

                logger.info("Application closed")

                end_time = datetime.now()

                session_time = end_time - self.start_time

                minutes = session_time.seconds // 60
                seconds = session_time.seconds % 60

                print("\n" + "=" * 40)
                print("Today's Session")
                print("=" * 40)

                print(f"Questions Asked : {self.question_count}")
                print(f"Session Length : {minutes} min {seconds} sec")

                print("\nGoodbye!")

                break

            if question.lower() == "/history":
                self.show_history()
                continue

            if question.lower() == "/clear":
                self.clear_history()
                continue

            if question.lower() == "/help":

                logger.info("Help command used")

                print("""
========================================
        Available Commands
========================================

/help      Show this menu

/history   View conversation history

/clear     Clear current session

/save      Save chat history (JSON)

/exit      Exit application

========================================
""")
                continue

            if question.lower() == "/save":

                save_chat_json(self.history)

                logger.info("Chat history saved to JSON")

                print("✅ Chat saved successfully.")

                continue

            try:

                answer = self.generate_response(question)

                print(f"\n[{timestamp()}]")
                print("Assistant:", answer)

            except Exception as e:

                logger.error(f"Gemini API Error: {e}")

                print("Something went wrong.")
                print("Please try again.")