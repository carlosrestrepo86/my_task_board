from sqlmodel import SQLModel

class UserModel(SQLModel):
    username: str
    email: str
    password_hash: str
    