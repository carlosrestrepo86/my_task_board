from fastapi import APIRouter, status
from sqlalchemy import select
from app.db.db import SessionDb
from app.models.tag import Tag
from app.models.user import User
from app.schemas.tag import TagModel

def create_tag_db(user_data: TagModel,
               session: SessionDb,
               current_user: User):
    
    tag_db = Tag(**user_data.model_dump())
    
    session.add(tag_db)
    session.commit()
    session.refresh(tag_db)
    
    return tag_db

def list_tags_db(session: SessionDb):
    return session.exec(select(Tag)).scalars().all()