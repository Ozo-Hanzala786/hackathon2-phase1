from sqlmodel import SQLModel, Field, Column, DateTime
from typing import Optional
from datetime import datetime
import uuid


class TaskBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = Field(default=False)


class Task(TaskBase, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: str = Field(foreign_key="user.id", nullable=False)
    created_at: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), default=datetime.utcnow)
    )
    updated_at: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
    )


class TaskCreate(TaskBase):
    pass


class TaskUpdate(SQLModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: Optional[bool] = None


class TaskRead(TaskBase):
    id: uuid.UUID
    user_id: str
    created_at: datetime
    updated_at: datetime