from sqlalchemy import select
from app.core.security import get_password_hash, verify_password
from app.db.db import SessionDb
from app.schemas.user import UserModel, UserLogin
from app.models.user import User
from fastapi import APIRouter, HTTPException, status

def register_user_bd(user_data : UserModel,
                      session: SessionDb):
    
    # Create User with hash function
    user_db = User(
        username=user_data.username,
        email=user_data.email,
        password=get_password_hash(user_data.password)
    )
    
    existing_user = session.exec(select(User).where(User.email == user_data.email)).first()
    
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
    
    session.add(user_db)
    session.commit()
    session.refresh(user_db)
    
    return user_db

def get_user_by_id_bd(user_id: int,
                   session: SessionDb):
    
    user_db = session.get(User, user_id)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return user_db

