from fastapi import APIRouter, status
from app.CRUD.user import get_user_by_id_bd, list_users_db, register_user_bd
from app.db.db import SessionDb
from app.schemas.user import UserModel

router = APIRouter()

@router.post("/users", 
          response_model=UserModel, 
          status_code=status.HTTP_201_CREATED,
          tags=['Users'])
def register_user(user_data : UserModel,
                      session: SessionDb):
    return register_user_bd(user_data, session)

@router.get("/users/{user_id}",
            response_model=UserModel,
            tags=['Users'])
def get_user_by_id(user_id: int,
                   session: SessionDb):
    return get_user_by_id_bd(user_id, session)

@router.get("/users",
            response_model=list[UserModel],
            tags=['Users'])
def list_users(session: SessionDb):
    return list_users_db(session)