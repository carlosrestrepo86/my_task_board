from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Task(BaseModel):
    title: str
    description: Optional[str]
    due_date: Optional[datetime]
    priority: int #(1-5)
    is_completed: bool
    #user_id: FK -> Usuario
    #tags: ManyToMany -> Etiqueta