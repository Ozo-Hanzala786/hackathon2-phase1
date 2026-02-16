from typing import List, Optional
from sqlmodel import Session, select
from ..models.task import Task, TaskCreate, TaskUpdate
from uuid import UUID
from datetime import datetime


class TaskService:
    def __init__(self, session: Session):
        self.session = session

    def create_task(self, task_data: TaskCreate, user_id: str) -> Task:
        """
        Create a new task for a user
        """
        task = Task.model_validate(task_data)
        task.user_id = user_id
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task

    def get_tasks_by_user(self, user_id: str) -> List[Task]:
        """
        Get all tasks for a specific user
        """
        statement = select(Task).where(Task.user_id == user_id)
        tasks = self.session.exec(statement).all()
        return tasks

    def get_task_by_id(self, task_id: UUID, user_id: str) -> Optional[Task]:
        """
        Get a specific task by ID for a specific user
        """
        statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        task = self.session.exec(statement).first()
        return task

    def update_task(self, task_id: UUID, task_data: TaskUpdate, user_id: str) -> Optional[Task]:
        """
        Update a specific task for a user
        """
        task = self.get_task_by_id(task_id, user_id)
        if task:
            for field, value in task_data.model_dump(exclude_unset=True).items():
                setattr(task, field, value)
            task.updated_at = datetime.utcnow()
            self.session.add(task)
            self.session.commit()
            self.session.refresh(task)
        return task

    def delete_task(self, task_id: UUID, user_id: str) -> bool:
        """
        Delete a specific task for a user
        """
        task = self.get_task_by_id(task_id, user_id)
        if task:
            self.session.delete(task)
            self.session.commit()
            return True
        return False

    def toggle_task_completion(self, task_id: UUID, completed: bool, user_id: str) -> Optional[Task]:
        """
        Toggle the completion status of a task
        """
        task = self.get_task_by_id(task_id, user_id)
        if task:
            task.completed = completed
            task.updated_at = datetime.utcnow()
            self.session.add(task)
            self.session.commit()
            self.session.refresh(task)
        return task