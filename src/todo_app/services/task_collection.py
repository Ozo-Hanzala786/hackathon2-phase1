"""
TaskCollection for managing tasks with JSON file persistence
"""
import json
import os
from typing import Dict, List, Optional
from ..models.task import Task


class TaskCollection:
    """
    Collection class to manage tasks with JSON file persistence.
    """

    def __init__(self, storage_file: str = "tasks.json"):
        """
        Initialize the collection and load tasks from file.
        
        Args:
            storage_file: Path to the JSON file for storing tasks
        """
        self.storage_file = storage_file
        self._tasks: Dict[str, Task] = {}
        self._load_from_file()

    def _load_from_file(self):
        """Load tasks from the JSON file if it exists."""
        if not os.path.exists(self.storage_file):
            return

        try:
            with open(self.storage_file, 'r') as f:
                data = json.load(f)
                for task_data in data:
                    # Handle potential missing fields or format changes gracefully
                    try:
                        task = Task(
                            id=task_data['id'],
                            title=task_data['title'],
                            description=task_data.get('description', ''),
                            completed=task_data.get('completed', False)
                        )
                        self._tasks[task.id] = task
                    except (KeyError, ValueError):
                        continue
        except (json.JSONDecodeError, IOError):
            # If (file is corrupted or unreadable, start with empty list
            pass

    def _save_to_file(self):
        """Save all tasks to the JSON file."""
        data = [
            {
                'id': t.id,
                'title': t.title,
                'description': t.description,
                'completed': t.completed
            }
            for t in self._tasks.values()
        ]
        
        try:
            with open(self.storage_file, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError:
            # In a real app we might want to log this or raise an error
            pass

    def add(self, task: Task) -> bool:
        """
        Add a task to the collection and save to file.

        Args:
            task: The task to add

        Returns:
            True if the task was added, False if ID already exists
        """
        if task.id in self._tasks:
            return False
        self._tasks[task.id] = task
        self._save_to_file()
        return True

    def get_all(self) -> List[Task]:
        """
        Retrieve all tasks in the collection.

        Returns:
            A list of all tasks
        """
        return list(self._tasks.values())

    def get_by_id(self, task_id: str) -> Optional[Task]:
        """
        Get a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The task if found, None otherwise
        """
        return self._tasks.get(task_id)

    def update(self, task_id: str, task: Task) -> bool:
        """
        Update a task in the collection and save to file.

        Args:
            task_id: The ID of the task to update
            task: The updated task object

        Returns:
            True if the task was updated, False if not found
        """
        if task_id in self._tasks:
            self._tasks[task_id] = task
            self._save_to_file()
            return True
        return False

    def delete(self, task_id: str) -> bool:
        """
        Delete a task from the collection and save to file.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False if not found
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            self._save_to_file()
            return True
        return False

    def exists(self, task_id: str) -> bool:
        """
        Check if a task exists in the collection.

        Args:
            task_id: The ID of the task to check

        Returns:
            True if the task exists, False otherwise
        """
        return task_id in self._tasks

    def count(self) -> int:
        """
        Get the total number of tasks in the collection.

        Returns:
            The number of tasks
        """
        return len(self._tasks)

    def clear(self):
        """Clear all tasks from the collection and the file."""
        self._tasks.clear()
        self._save_to_file()