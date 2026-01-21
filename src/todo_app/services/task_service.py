"""
TaskService for managing tasks in memory
"""
import uuid
from typing import List, Optional
from ..models.task import Task
from .task_collection import TaskCollection


class TaskService:
    """
    Business logic for task operations with in-memory storage.
    """

    def __init__(self):
        """Initialize the service with a TaskCollection."""
        self._collection = TaskCollection()

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task with a unique ID.

        Args:
            title: The title of the task
            description: The description of the task (optional)

        Returns:
            The created Task object

        Raises:
            ValueError: If the title is empty or whitespace-only
        """
        # Validate input
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty or whitespace-only")

        # Generate unique ID
        task_id = str(uuid.uuid4())

        # Create and store the task
        task = Task(id=task_id, title=title, description=description, completed=False)
        self._collection.add(task)

        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks.

        Returns:
            A list of all tasks in the collection
        """
        return self._collection.get_all()

    def get_task_by_id(self, task_id: str) -> Optional[Task]:
        """
        Find a task by its ID.

        Args:
            task_id: The ID of the task to find

        Returns:
            The task if found, None otherwise
        """
        return self._collection.get_by_id(task_id)

    def update_task(self, task_id: str, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
        """
        Update an existing task.

        Args:
            task_id: The ID of the task to update
            title: The new title (optional)
            description: The new description (optional)

        Returns:
            The updated task if found, None otherwise

        Raises:
            ValueError: If the title is empty or whitespace-only
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return None

        # Validate new title if provided
        if title is not None:
            if not title or not title.strip():
                raise ValueError("Task title cannot be empty or whitespace-only")
            task.title = title

        # Update description if provided
        if description is not None:
            task.description = description

        # Update the task in collection
        self._collection.update(task_id, task)
        return task

    def delete_task(self, task_id: str) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False if not found
        """
        return self._collection.delete(task_id)

    def mark_complete(self, task_id: str) -> bool:
        """
        Mark a task as complete.

        Args:
            task_id: The ID of the task to mark complete

        Returns:
            True if the task was found and updated, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = True
            # Update the task in collection
            self._collection.update(task_id, task)
            return True
        return False

    def mark_incomplete(self, task_id: str) -> bool:
        """
        Mark a task as incomplete.

        Args:
            task_id: The ID of the task to mark incomplete

        Returns:
            True if the task was found and updated, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = False
            # Update the task in collection
            self._collection.update(task_id, task)
            return True
        return False

    def get_task_count(self) -> int:
        """
        Get the total number of tasks.

        Returns:
            The number of tasks in the collection
        """
        return self._collection.count()