# AI Career Assistant

AI Career Assistant is a command-line application built with Python and the Google Gemini API. It provides AI-powered career guidance while demonstrating clean software engineering practices, modular project design, structured logging, and session management.

---

## Features

- AI-powered career coaching using Google Gemini
- Interactive command-line interface
- Session-based conversation history
- Search previous conversations by keyword
- Export conversations to Markdown
- Save conversations as JSON
- Session statistics (questions asked and duration)
- Timestamped responses
- Structured logging
- Exception handling with user-friendly messages
- Type hints and docstrings
- Object-oriented architecture using classes and dataclasses
- Configurable application settings

---

## Technologies Used

- Python 3
- Google Gemini API
- Dataclasses
- Enum
- Logging
- JSON
- Pathlib
- dotenv

---

## Project Structure

```text
AI-Career-Assistant/
│
├── main.py
├── career_assistant.py
├── config.py
├── constants.py
├── models.py
├── logger.py
├── utils.py
│
├── history/
├── exports/
├── logs/
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/AI-Career-Assistant.git
```

Navigate to the project directory:

```bash
cd AI-Career-Assistant
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Running the Application

```bash
python main.py
```

---

## Available Commands

| Command | Description |
|---------|-------------|
| `/help` | Display available commands |
| `/history` | View conversation history |
| `/search <keyword>` | Search previous conversations |
| `/save` | Save conversation history as JSON |
| `/export` | Export the current session as Markdown |
| `/clear` | Clear the current session history |
| `/exit` | Exit the application |

---

## Software Engineering Concepts Demonstrated

This project applies several software engineering concepts, including:

- Object-Oriented Programming (OOP)
- Dataclasses
- Enumerations (Enum)
- Type Hints
- Docstrings
- Exception Handling
- Logging
- Configuration Management
- JSON Serialization
- File Management
- Modular Project Structure

---

## Future Enhancements

- FastAPI web interface
- Database integration
- User authentication
- Retrieval-Augmented Generation (RAG)
- Persistent chat memory
- Multi-user support
- Streaming AI responses

---

## Author

**Memoona Shahid**

Computer Science Student | Aspiring AI Engineer

This project was developed as part of my AI Engineering learning journey to gain practical experience in building production-style AI applications using Python and Large Language Models.
