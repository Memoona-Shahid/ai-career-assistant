from datetime import datetime


def print_banner():
    print("=" * 50)
    print("🤖 AI Career Assistant")
    print("Powered by Gemini")
    print("=" * 50)
    print("Type /help to see available commands.\n")


def print_help():
    print("""
Available Commands

/help      Show commands
/history   Show chat history
/clear     Clear history
/exit      Exit program
""")


def show_history(history):

    if not history:
        print("\nNo history yet.")
        return

    print("\nConversation History")
    print("-" * 50)

    for i, chat in enumerate(history, start=1):

        print(f"\n[{chat['time']}]")
        print(f"Q{i}: {chat['question']}")
        print(f"A{i}: {chat['answer']}")


def save_chat_history(question, answer, timestamp):

    with open("history.txt", "a", encoding="utf-8") as file:

        file.write("=" * 60 + "\n")
        file.write(f"[{timestamp}]\n\n")
        file.write(f"Question:\n{question}\n\n")
        file.write(f"Answer:\n{answer}\n")
        file.write("=" * 60 + "\n\n")