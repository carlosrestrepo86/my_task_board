from sqlalchemy import select
from app.db.db import SessionDb
from app.schemas.user import UserModel
from app.models.user import User
from fastapi import APIRouter, HTTPException, status

router = APIRouter()

@router.post("/registers", 
          response_model=UserModel, 
          status_code=status.HTTP_201_CREATED,
          tags=['Registers'])
def register_user(user_data : UserModel,
                      session: SessionDb):
    
    user_db = User(**user_data.model_dump())
    
    existing_user = session.exec(select(User).where(User.email == user_data.email)).first()
    
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")
    
    session.add(user_db)
    session.commit()
    session.refresh(user_db)
    
    return user_db