"""
Task model representing a single todo item
"""
import uuid
from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a single todo item with a unique ID, title, description, and completion status.
    """
    id: str
    title: str
    description: Optional[str] = ""
    completed: bool = False

    def __post_init__(self):
        """Validate the task after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Task title cannot be empty or whitespace-only")
        if not isinstance(self.completed, bool):
            raise ValueError("Completed status must be boolean")