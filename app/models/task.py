from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field
from app.models.user import User

class TaskBase(SQLModel):
    title: str = Field(default=None)
    description: Optional[str] = Field(default=None)
    due_date: Optional[datetime] = Field(default=None)
    priority: int = Field(default=None) # 1 - 5
    is_completed: bool = Field(default=None)
    
class CreateTask(TaskBase):
    pass

class Task(TaskBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None, foreign_key="user.id")
    # Falta tags