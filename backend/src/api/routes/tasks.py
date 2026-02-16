from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List
from ...database import get_session
from ...services.task_service import TaskService
from ...models.task import Task, TaskCreate, TaskUpdate, TaskRead
from ..deps import get_current_user_id, verify_user_id_match

router = APIRouter()


@router.get("/tasks", response_model=List[TaskRead])
def get_tasks(user_id: str, current_user_id: str = Depends(verify_user_id_match), db: Session = Depends(get_session)):
    """
    Get all tasks for the authenticated user
    """
    task_service = TaskService(db)
    tasks = task_service.get_tasks_by_user(user_id=current_user_id)
    return tasks


@router.post("/tasks", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(user_id: str, task_data: TaskCreate, current_user_id: str = Depends(verify_user_id_match), db: Session = Depends(get_session)):
    """
    Create a new task for the authenticated user
    """
    task_service = TaskService(db)
    task = task_service.create_task(task_data=task_data, user_id=current_user_id)
    return task


@router.get("/tasks/{task_id}", response_model=TaskRead)
def get_task(user_id: str, task_id: str, current_user_id: str = Depends(verify_user_id_match), db: Session = Depends(get_session)):
    """
    Get a specific task by ID for the authenticated user
    """
    task_service = TaskService(db)
    task = task_service.get_task_by_id(task_id=task_id, user_id=current_user_id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or does not belong to user"
        )

    return task


@router.put("/tasks/{task_id}", response_model=TaskRead)
def update_task(user_id: str, task_id: str, task_data: TaskUpdate, current_user_id: str = Depends(verify_user_id_match), db: Session = Depends(get_session)):
    """
    Update a specific task for the authenticated user
    """
    task_service = TaskService(db)
    task = task_service.update_task(task_id=task_id, task_data=task_data, user_id=current_user_id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or does not belong to user"
        )

    return task


@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(user_id: str, task_id: str, current_user_id: str = Depends(verify_user_id_match), db: Session = Depends(get_session)):
    """
    Delete a specific task for the authenticated user
    """
    task_service = TaskService(db)
    success = task_service.delete_task(task_id=task_id, user_id=current_user_id)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or does not belong to user"
        )

    return {"detail": "Task deleted successfully"}


@router.patch("/tasks/{task_id}/complete", response_model=TaskRead)
def toggle_task_completion(user_id: str, task_id: str, completed: bool, current_user_id: str = Depends(verify_user_id_match), db: Session = Depends(get_session)):
    """
    Toggle the completion status of a task for the authenticated user
    """
    task_service = TaskService(db)
    task = task_service.toggle_task_completion(task_id=task_id, completed=completed, user_id=current_user_id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found or does not belong to user"
        )

    return task