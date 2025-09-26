from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.CRUD.auth import login_db
from app.db.db import SessionDb

router = APIRouter()

@router.post("/auth/login",
             tags=['Auth'])
def login(session: SessionDb,
          user_data: OAuth2PasswordRequestForm = Depends()):
    return login_db(user_data, session)
