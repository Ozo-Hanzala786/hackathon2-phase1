"""
Unit tests for TaskService error handling and validation
"""
import pytest
from src.todo_app.services.task_service import TaskService


def test_add_task_with_empty_title_raises_error():
    """Test that adding a task with empty title raises ValueError."""
    service = TaskService()

    with pytest.raises(ValueError, match="Task title cannot be empty or whitespace-only"):
        service.add_task("")


def test_add_task_with_whitespace_only_title_raises_error():
    """Test that adding a task with whitespace-only title raises ValueError."""
    service = TaskService()

    with pytest.raises(ValueError, match="Task title cannot be empty or whitespace-only"):
        service.add_task("   ")


def test_update_task_with_empty_title_raises_error():
    """Test that updating a task with empty title raises ValueError."""
    service = TaskService()

    # Add a valid task first
    task = service.add_task("Original Title", "Description")

    # Attempt to update with empty title
    with pytest.raises(ValueError, match="Task title cannot be empty or whitespace-only"):
        service.update_task(task.id, "")


def test_update_nonexistent_task_returns_none():
    """Test that updating a non-existent task returns None."""
    service = TaskService()

    result = service.update_task("nonexistent_id", "New Title")
    assert result is None


def test_delete_nonexistent_task_returns_false():
    """Test that deleting a non-existent task returns False."""
    service = TaskService()

    result = service.delete_task("nonexistent_id")
    assert result is False


def test_mark_complete_nonexistent_task_returns_false():
    """Test that marking complete a non-existent task returns False."""
    service = TaskService()

    result = service.mark_complete("nonexistent_id")
    assert result is False


def test_mark_incomplete_nonexistent_task_returns_false():
    """Test that marking incomplete a non-existent task returns False."""
    service = TaskService()

    result = service.mark_incomplete("nonexistent_id")
    assert result is False


def test_get_task_by_nonexistent_id_returns_none():
    """Test that getting a non-existent task returns None."""
    service = TaskService()

    result = service.get_task_by_id("nonexistent_id")
    assert result is None