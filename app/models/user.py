from pydantic import EmailStr
from sqlmodel import SQLModel, Field
from datetime import datetime

class UserBase(SQLModel):
    username: str = Field(default=None)
    email: EmailStr  = Field(default=None)
    password_hash: str = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.now)
    
class CreateUser(UserBase):
    pass

class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

