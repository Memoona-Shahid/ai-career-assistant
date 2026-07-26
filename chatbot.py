from config import client
from utils import print_help, show_history

history = []


def ask_gemini(question):

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"""
You are an experienced AI Career Coach.

Answer professionally.

Question:
{question}
"""
    )

    return response.text


def chat():

    while True:

        question = input("\nYou: ")

        if question.lower() == "/exit":

            print("\nConversation Summary")
            show_history(history)
            break

        if question.lower() == "/help":
            print_help()
            continue

        if question.lower() == "/history":
            show_history(history)
            continue

        if question.lower() == "/clear":
            history.clear()
            print("History cleared.")
            continue

        try:

            answer = ask_gemini(question)

            print("\nAssistant:", answer)

            history.append({
                "question": question,
                "answer": answer
            })

        except Exception as e:
            print(e)