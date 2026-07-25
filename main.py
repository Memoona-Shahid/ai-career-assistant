from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Read API key
API_KEY = os.getenv("GEMINI_API_KEY")

# Check if API key exists
if not API_KEY:
    print("API Key not found!")
    exit()

# Create Gemini client
client = genai.Client(api_key=API_KEY)

# Store conversation
history = []

print("=" * 50)
print("🤖 AI Career Assistant")
print("Type /help to see available commands.")
print("=" * 50)

while True:

    question = input("\nYou: ")

    # Exit
    if question.lower() == "/exit":
        print("\nConversation Summary")
        print("-" * 40)

        if len(history) == 0:
            print("No conversation found.")

        else:
            for i, chat in enumerate(history, start=1):
                print(f"\nQ{i}: {chat['question']}")
                print(f"A{i}: {chat['answer']}")

        print("\nGoodbye!")
        break

    # Help
    if question.lower() == "/help":
        print("""
Available Commands

/help      Show commands
/history   Show conversation history
/clear     Clear history
/exit      Exit program
""")
        continue

    # History
    if question.lower() == "/history":

        if len(history) == 0:
            print("No history yet.")

        else:
            print("\nConversation History")
            print("-" * 40)

            for i, chat in enumerate(history, start=1):
                print(f"\nQ{i}: {chat['question']}")
                print(f"A{i}: {chat['answer']}")

        continue

    # Clear
    if question.lower() == "/clear":
        history.clear()
        print("Conversation history cleared.")
        continue

    # Send request to Gemini
    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=f"""
You are an experienced career coach helping Computer Science students become AI Engineers.

Rules:
- Give practical advice.
- Keep answers concise.
- Suggest projects when helpful.

User Question:
{question}
"""
        )

        answer = response.text

        print("\nAssistant:", answer)

        # Save history
        history.append({
            "question": question,
            "answer": answer
        })

    except Exception as e:
        print("\nError:", e)