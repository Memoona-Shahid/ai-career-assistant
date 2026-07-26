def print_banner():
    print("=" * 50)
    print("🤖 AI Career Assistant")
    print("Type /help to see available commands.")
    print("=" * 50)


def print_help():
    print("""
Available Commands

/help
/history
/clear
/exit
""")


def show_history(history):

    if not history:
        print("No history yet.")
        return

    print("\nConversation History")
    print("-" * 40)

    for i, chat in enumerate(history, start=1):
        print(f"\nQ{i}: {chat['question']}")
        print(f"A{i}: {chat['answer']}")