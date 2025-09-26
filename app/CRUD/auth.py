from datetime import timedelta
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from app.core.security import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, verify_password
from app.db.db import SessionDb
from app.models.user import User

def login_db(user_data: OAuth2PasswordRequestForm,
          session: SessionDb):
    
    user_db = session.exec(select(User).where(User.email == user_data.username)).scalars().first()
    if not user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    verify_hash = verify_password(user_data.password, user_db.password)
    if not verify_hash:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(data={"sub": str(user_db.id)}, expires_delta=access_token_expires)
    
    return {"access_token": token, "token_type": "bearer"}