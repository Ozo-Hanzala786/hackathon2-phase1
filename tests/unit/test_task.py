"""
Unit tests for Task model validation
"""
import pytest
from src.todo_app.models.task import Task


def test_task_creation_with_valid_data_succeeds():
    """Test that creating a task with valid data succeeds."""
    task = Task(id="123", title="Valid Title", description="Valid Description", completed=False)

    assert task.id == "123"
    assert task.title == "Valid Title"
    assert task.description == "Valid Description"
    assert task.completed is False


def test_task_creation_with_empty_title_raises_error():
    """Test that creating a task with empty title raises ValueError."""
    with pytest.raises(ValueError, match="Task title cannot be empty or whitespace-only"):
        Task(id="123", title="", description="Valid Description", completed=False)


def test_task_creation_with_whitespace_only_title_raises_error():
    """Test that creating a task with whitespace-only title raises ValueError."""
    with pytest.raises(ValueError, match="Task title cannot be empty or whitespace-only"):
        Task(id="123", title="   ", description="Valid Description", completed=False)


def test_task_creation_with_invalid_completed_status_raises_error():
    """Test that creating a task with non-boolean completed status raises ValueError."""
    with pytest.raises(ValueError, match="Completed status must be boolean"):
        Task(id="123", title="Valid Title", description="Valid Description", completed="invalid")