from fastapi import HTTPException, status
from fastapi_filter import FilterDepends
from sqlmodel import select
from app.db.db import SessionDb
from app.filters import TaskFilter
from app.models.tag import Tag
from app.models.task import Task
from app.models.user import User
from app.schemas.task import TaskModel, TaskUpdate

def create_task_db(user_data: TaskModel,
               session: SessionDb,
               current_user: User):
    
    user = session.exec(select(User).where(User.id == user_data.user_id)).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    task_db = Task(**user_data.model_dump()) 
    
    session.add(task_db)
    session.commit()
    session.refresh(task_db)
    
    return task_db

def delete_task_db(task_id: int,
                session: SessionDb,
                current_user: User):
    
    task_db = session.get(Task, task_id)
    if not task_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    
    session.delete(task_db)
    session.commit()
    
    return {"Message": f"Task with id {task_id} deleted successfully"}

def update_task_db(task_id: int, 
                   user_data: TaskUpdate,
                   session: SessionDb,
                   current_user: User):
    
    task_db = session.get(Task, task_id)
    if not task_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    
    data = user_data.model_dump(exclude_unset=True)
    task_db.sqlmodel_update(data)
    session.add(task_db)
    session.commit()
    session.refresh(task_db)
    
    return task_db

def list_tasks_by_filter_db(session: SessionDb, 
                           task_filter = FilterDepends(TaskFilter)): 
     
    query = task_filter.filter(select(Task))
    
    return session.exec(query).all()

def add_tag_to_task_bd(task_id: int,
                       tag_id: int, 
                       session: SessionDb,
                       current_user: User):
    
    task_db = session.get(Task, task_id)
    if not task_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    
    tag_db = session.get(Tag, tag_id)
    if not tag_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found")
    
    if tag_db in task_db.tags:
        return {"message": "Tag already related to this task"}
    
    task_db.tags.append(tag_db)
    session.add(task_db)
    session.commit()
    session.refresh(task_db)
    
    return {"message": f"Tag {tag_db.name} added to Task {task_db.title}"}

def delete_tag_to_task_bd(task_id: int,
                          tag_id: int, 
                          session: SessionDb,
                          current_user: User):
    
    task_db = session.get(Task, task_id)
    if not task_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    
    tag_db = session.get(Tag, tag_id)
    if not tag_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    
    if not tag_db in task_db.tags:
        return {"message": "Tag not related to this task"}
    
    task_db.tags.remove(tag_db)
    
    session.add(task_db)
    session.commit()
    session.refresh(task_db)
    
    return {"message": f"Tag {tag_id} removed from Task {task_id}"}