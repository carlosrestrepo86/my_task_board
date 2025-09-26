from typing import Optional
from pydantic import BaseModel

class TagModel(BaseModel):
    name: str
    
class TagUpdate(BaseModel):
    name: Optional[str]