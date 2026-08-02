from enum import Enum

# ======================================================
# Application
# ======================================================

APP_NAME = "AI Career Assistant"

DEFAULT_MODEL = "gemini-3.5-flash"

MAX_HISTORY = 20

# ======================================================
# Commands
# ======================================================


class Command(Enum):
    HELP = "/help"
    HISTORY = "/history"
    CLEAR = "/clear"
    SAVE = "/save"
    EXPORT = "/export"
    EXIT = "/exit"