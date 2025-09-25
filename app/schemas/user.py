from pydantic import EmailStr
from sqlmodel import SQLModel

class UserModel(SQLModel):
    username: str
    email: EmailStr
    password: str
    
class UserLogin(SQLModel):
    email: EmailStr
    password: str