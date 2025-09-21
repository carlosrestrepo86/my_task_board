from fastapi import APIRouter, HTTPException, status
from fastapi_filter import FilterDepends
from sqlmodel import select
from app.db.db import SessionDb
from app.filters import TaskFilter
from app.models.tag import Tag
from app.models.task import Task
from app.models.user import User
from app.schemas.task import TaskModel, TaskUpdate

router = APIRouter()

@router.post("/tasks", 
          response_model=TaskModel, 
          status_code=status.HTTP_201_CREATED,
          tags=['Tasks'])
def create_task(user_data: TaskModel,
               session: SessionDb):
    
    user = session.exec(select(User).where(User.id == user_data.user_id)).first()
    print("User: ", user)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    task_db = Task(**user_data.model_dump()) 
    
    session.add(task_db)
    session.commit()
    session.refresh(task_db)
    
    return task_db

@router.delete("/tasks/{task_id}", tags=['Tasks'])
def delete_task(task_id: int,
                session: SessionDb):
    
    task_db = session.get(Task, task_id)
    if not task_db:
        raise HTTPException(status_code=404, detail="Task not found")
    
    session.delete(task_db)
    session.commit()
    
    return {"Message": f"Task with id {task_id} deleted successfully"}

@router.patch("/tasks/{task_id}", 
          response_model=TaskModel, 
          status_code=status.HTTP_201_CREATED,
          tags=['Tasks'])
def update_task(task_id: int, user_data: TaskUpdate, session: SessionDb):
    
    task_db = session.get(Task, task_id)
    if not task_db:
        raise HTTPException(status_code=404, detail="Task not found")
    
    data = user_data.model_dump(exclude_unset=True)
    task_db.sqlmodel_update(data)
    session.add(task_db)
    session.commit()
    session.refresh(task_db)
    return task_db

@router.get("/tasks",
            response_model=list[Task],
            tags=['Tasks'])
def list_tasks_by_filter(session: SessionDb, 
                           task_filter = FilterDepends(TaskFilter)): 
     
    query = task_filter.filter(select(Task))
    
    return session.exec(query).all()

@router.post("/tasks/{task_id}/add-tag/{tag_id}",
             tags=['Tasks'])
def add_tag_to_task(task_id: int,
                    tag_id: int, session: SessionDb):
    
    task_db = session.get(Task, task_id)
    if not task_db:
        raise HTTPException(status_code=404, detail="Task not found")
    
    tag_db = session.get(Tag, tag_id)
    if not tag_db:
        raise HTTPException(status_code=404, detail="Task not found")
    
    if tag_db in task_db.tags:
        return {"message": "Tag already related to this task"}
    
    task_db.tags.append(tag_db)
    session.add(task_db)
    session.commit()
    session.refresh(task_db)
    
    return {"message": f"Tag {tag_db.name} added to Task {task_db.title}"}
    