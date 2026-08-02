from pathlib import Path
import os

from dotenv import load_dotenv
from google import genai

from constants import DEFAULT_MODEL

# ======================================================
# Load Environment Variables
# ======================================================

load_dotenv()

# ======================================================
# Project Paths
# ======================================================

BASE_DIR = Path(__file__).parent

LOG_DIR = BASE_DIR / "logs"
HISTORY_DIR = BASE_DIR / "history"
EXPORT_DIR = BASE_DIR / "exports"

LOG_DIR.mkdir(exist_ok=True)
HISTORY_DIR.mkdir(exist_ok=True)
EXPORT_DIR.mkdir(exist_ok=True)

# ======================================================
# Gemini Configuration
# ======================================================

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file."
    )

MODEL_NAME = DEFAULT_MODEL

client = genai.Client(api_key=API_KEY)