from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel

class TaskModel(SQLModel):
    title: str
    description: Optional[str]
    due_date: Optional[datetime]
    priority: int #(1-5)
    is_completed: bool
    user_id: int # FK -> Usuario
    #tags: ManyToMany -> Etiqueta
    
class TaskUpdate(SQLModel):
    title: Optional[str]
    description: Optional[str]
    due_date: Optional[datetime]
    priority: Optional[int] #(1-5)
    is_completed: Optional[bool]
    user_id: Optional[int] # FK -> Usuario
    #tags: ManyToMany -> Etiqueta
    