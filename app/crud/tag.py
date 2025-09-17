from fastapi import APIRouter, status
from sqlalchemy import select
from app.db.db import SessionDb
from app.models.tag import Tag
from app.schemas.tag import TagModel

router = APIRouter()

@router.post("/tags/create", 
          response_model=TagModel, 
          status_code=status.HTTP_201_CREATED,
          tags=['Tags'])
def create_tag(user_data: TagModel,
               session: SessionDb):
    
    tag_db = Tag(**user_data.model_dump())
    
    session.add(tag_db)
    session.commit()
    session.refresh(tag_db)
    
    return tag_db

@router.get("/tags/list",
            response_model=list[Tag],
            tags=['Tags'])
def list_tags(session: SessionDb):
    return session.exec(select(Tag)).scalars().all()