from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from app.db.db import SessionDb
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
def list_tasks(session: SessionDb):
    return session.exec(select(Task)).all()
    