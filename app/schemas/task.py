from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel

class Task(SQLModel):
    title: str
    description: Optional[str]
    due_date: Optional[datetime]
    priority: int #(1-5)
    is_completed: bool
    #user_id: FK -> Usuario
    #tags: ManyToMany -> Etiqueta