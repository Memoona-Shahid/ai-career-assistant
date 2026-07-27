from config import client
from utils import timestamp
from logger import save_history, logger


class CareerAssistant:

    def __init__(self):
        self.history = []
        self.question_count = 0

    def generate_response(self, question):

        # Log user question
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

        # Log successful response
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

                print(f"\nQuestions Asked: {self.question_count}")
                print("Goodbye!")
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
Commands

/help
/history
/clear
/exit
""")
                continue

            try:

                answer = self.generate_response(question)

                print(f"\n[{timestamp()}]")
                print("Assistant:", answer)

            except Exception as e:

                logger.error(f"Gemini API Error: {e}")

                print("Something went wrong.")