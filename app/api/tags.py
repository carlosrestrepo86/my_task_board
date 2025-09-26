from fastapi import APIRouter, Depends, status
from app.CRUD.tag import create_tag_db, delete_tag_db, list_tags_db, update_tag_db
from app.core.dependencies import get_current_user
from app.db.db import SessionDb
from app.models.tag import Tag
from app.models.user import User
from app.schemas.tag import TagModel, TagUpdate


router = APIRouter()

@router.post("/tags", 
          response_model=TagModel, 
          status_code=status.HTTP_201_CREATED,
          tags=['Tags'])
def create_tag(user_data: TagModel,
               session: SessionDb,
               current_user: User = Depends(get_current_user)):
    return create_tag_db(user_data, session, current_user)

@router.get("/tags",
            response_model=list[Tag],
            tags=['Tags'])
def list_tags(session: SessionDb):
    return list_tags_db(session)

@router.delete("/tags/{tag_id}",
               tags=['Tags'])
def delete_tag(tag_id: int,
               session: SessionDb,
               current_user: User = Depends(get_current_user)):
    return delete_tag_db(tag_id, session, current_user)

@router.patch("/tags/{tag_id}",
              response_model=TagModel,
              status_code=status.HTTP_201_CREATED,
              tags=['Tags'])
def update_tag(tag_id: int,
               user_data: TagUpdate,
               session: SessionDb,
               current_user: User = Depends(get_current_user)):
    return update_tag_db(tag_id, user_data, session, current_user)