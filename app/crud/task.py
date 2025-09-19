from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from app.db.db import SessionDb
from app.models.task import Task
from app.models.user import User
from app.schemas.task import TaskModel

router = APIRouter()

@router.post("/tasks/create", 
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
    