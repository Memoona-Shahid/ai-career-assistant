from datetime import datetime

from config import client
from utils import (
    print_help,
    show_history,
    save_chat_history,
)

chat_history = []
question_count = 0


def ask_gemini(user_question):

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"""
You are an experienced AI Career Coach helping Computer Science students become AI Engineers.

Rules:
- Give practical advice.
- Keep answers concise.
- Suggest projects when helpful.

User Question:
{user_question}
"""
    )

    return response.text


def chat():

    global question_count

    while True:

        user_question = input("\nYou: ")

        if user_question.lower() == "/exit":

            print("\nConversation Summary")
            show_history(chat_history)

            print(f"\nQuestions Asked: {question_count}")

            print("\nGoodbye!")
            break

        if user_question.lower() == "/help":
            print_help()
            continue

        if user_question.lower() == "/history":
            show_history(chat_history)
            continue

        if user_question.lower() == "/clear":
            chat_history.clear()
            print("Conversation history cleared.")
            continue

        question_count += 1

        try:

            assistant_response = ask_gemini(user_question)

            timestamp = datetime.now().strftime("%I:%M %p")

            print(f"\n[{timestamp}]")
            print("Assistant:", assistant_response)

            chat_history.append(
                {
                    "question": user_question,
                    "answer": assistant_response,
                    "time": timestamp,
                }
            )

            save_chat_history(
                user_question,
                assistant_response,
                timestamp,
            )

        except Exception:

            print("\nSomething went wrong.")
            print("Please try again.")