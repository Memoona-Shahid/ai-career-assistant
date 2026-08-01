from pathlib import Path
from dotenv import load_dotenv
from google import genai
import os

# Load environment variables
load_dotenv()

# ======================================================
# Project Paths
# ======================================================

BASE_DIR = Path(__file__).parent

LOG_DIR = BASE_DIR / "logs"
HISTORY_DIR = BASE_DIR / "history"

LOG_DIR.mkdir(exist_ok=True)
HISTORY_DIR.mkdir(exist_ok=True)

# ======================================================
# Application Settings
# ======================================================

APP_NAME = "AI Career Assistant"

MODEL_NAME = "gemini-3.5-flash"

MAX_HISTORY = 100

# ======================================================
# Gemini Configuration
# ======================================================

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file."
    )

client = genai.Client(api_key=API_KEY)