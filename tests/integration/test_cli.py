"""
Integration tests for the CLI functionality
"""
import subprocess
import sys
import tempfile
import os
from unittest.mock import patch
import io


def test_add_and_list_tasks():
    """Test adding a task and then listing it."""
    # Since the CLI operates on in-memory data, we can't easily test end-to-end
    # through subprocess calls. Instead, we'll test the service directly.
    from src.todo_app.services.task_service import TaskService

    service = TaskService()

    # Add a task
    task = service.add_task("Test Task", "This is a test task")

    # Verify the task was added
    assert task.title == "Test Task"
    assert task.description == "This is a test task"
    assert task.completed is False

    # Get all tasks
    tasks = service.get_all_tasks()

    # Verify the task is in the list
    assert len(tasks) == 1
    assert tasks[0].id == task.id
    assert tasks[0].title == "Test Task"


def test_update_task():
    """Test updating a task."""
    from src.todo_app.services.task_service import TaskService

    service = TaskService()

    # Add a task
    original_task = service.add_task("Original Task", "Original description")

    # Update the task
    updated_task = service.update_task(original_task.id, "Updated Task", "Updated description")

    # Verify the task was updated
    assert updated_task.title == "Updated Task"
    assert updated_task.description == "Updated description"


def test_delete_task():
    """Test deleting a task."""
    from src.todo_app.services.task_service import TaskService

    service = TaskService()

    # Add a task
    task = service.add_task("Task to delete", "Description")

    # Verify the task exists
    assert len(service.get_all_tasks()) == 1

    # Delete the task
    result = service.delete_task(task.id)

    # Verify the task was deleted
    assert result is True
    assert len(service.get_all_tasks()) == 0


def test_mark_task_complete():
    """Test marking a task as complete."""
    from src.todo_app.services.task_service import TaskService

    service = TaskService()

    # Add a task
    task = service.add_task("Task to complete", "Description")

    # Verify it's initially incomplete
    assert task.completed is False

    # Mark as complete
    result = service.mark_complete(task.id)

    # Verify it's now complete
    assert result is True
    updated_task = service.get_task_by_id(task.id)
    assert updated_task.completed is True


def test_mark_task_incomplete():
    """Test marking a task as incomplete."""
    from src.todo_app.services.task_service import TaskService

    service = TaskService()

    # Add a task and mark it complete
    task = service.add_task("Task to mark incomplete", "Description")
    service.mark_complete(task.id)

    # Verify it's complete
    updated_task = service.get_task_by_id(task.id)
    assert updated_task.completed is True

    # Mark as incomplete
    result = service.mark_incomplete(task.id)

    # Verify it's now incomplete
    assert result is True
    updated_task = service.get_task_by_id(task.id)
    assert updated_task.completed is False