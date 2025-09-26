from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class TaskModel(BaseModel):
    title: str
    description: Optional[str]
    due_date: Optional[datetime]
    priority: int #(1-5)
    is_completed: bool = False
    user_id: int # FK -> User
    #tags: ManyToMany -> Tag
    
class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    due_date: Optional[datetime]
    priority: Optional[int] #(1-5)
    is_completed: Optional[bool]
    user_id: Optional[int] # FK -> User
    #tags: ManyToMany -> Tag
    