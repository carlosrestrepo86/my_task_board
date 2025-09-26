from fastapi import HTTPException, status
from sqlalchemy import select
from app.db.db import SessionDb
from app.models.tag import Tag
from app.models.user import User
from app.schemas.tag import TagModel, TagUpdate

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

def delete_tag_db(tag_id: int,
                  session: SessionDb,
                  current_user: User):
    
    tag_db = session.get(Tag, tag_id)
    if not tag_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found")
    
    session.delete(tag_db)
    session.commit()
    
    return {"Message": f"Tag with id {tag_id} deleted successfully"}

def update_tag_db(tag_id: int,
                  user_data: TagUpdate,
                  session: SessionDb,
                  current_user: User):
    
    tag_db = session.get(Tag, tag_id)
    if not tag_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found")
    
    data = user_data.model_dump(exclude_unset=True)
    tag_db.sqlmodel_update(data)
    
    session.add(tag_db)
    session.commit()
    session.refresh(tag_db)
    
    return tag_db
    