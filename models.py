from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ChatSession:
    """
    Represents a single chat session.
    """

    session_id: str
    created_at: datetime
    question_count: int = 0
    history: list = field(default_factory=list)