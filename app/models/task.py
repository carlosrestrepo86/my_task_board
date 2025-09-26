from datetime import datetime
from typing import TYPE_CHECKING, Optional
from sqlmodel import Relationship, SQLModel, Field
from app.models.link_table import TaskTagLink

if TYPE_CHECKING:
    from app.models.tag import Tag

class TaskBase(SQLModel):
    title: str = Field(default=None)
    description: Optional[str] = Field(default=None)
    due_date: Optional[datetime] = Field(default=None)
    priority: int = Field(default=None) # 1 - 5
    is_completed: bool = Field(default=False)
    
class CreateTask(TaskBase):
    pass

class Task(TaskBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None, foreign_key="user.id")
    tags: list["Tag"] = Relationship(back_populates="tasks", link_model=TaskTagLink)