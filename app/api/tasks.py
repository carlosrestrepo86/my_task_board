from fastapi import APIRouter, Depends, status
from fastapi_filter import FilterDepends
from app.CRUD.task import add_tag_to_task_bd, create_task_db, delete_tag_to_task_bd, delete_task_db, list_tasks_by_filter_db, update_task_db
from app.core.dependencies import get_current_user
from app.db.db import SessionDb
from app.filters import TaskFilter
from app.models.task import Task
from app.models.user import User
from app.schemas.task import TaskModel, TaskUpdate

router = APIRouter()

@router.post("/tasks",
          response_model=TaskModel, 
          status_code=status.HTTP_201_CREATED,
          tags=['Tasks'])
def create_task(session: SessionDb,
                user_data: TaskModel,
                current_user: User = Depends(get_current_user)):
    return create_task_db(user_data, session, current_user)

@router.delete("/tasks/{task_id}", tags=['Tasks'])
def delete_task(task_id: int,
                session: SessionDb,
                current_user: User = Depends(get_current_user)):
    return delete_task_db(task_id, session, current_user)

@router.patch("/tasks/{task_id}", 
          response_model=TaskModel, 
          status_code=status.HTTP_201_CREATED,
          tags=['Tasks'])
def update_task(task_id: int, 
                user_data: TaskUpdate, 
                session: SessionDb,
                current_user: User = Depends(get_current_user)):
    return update_task_db(task_id, user_data, session, current_user)

@router.get("/tasks",
            response_model=list[Task],
            tags=['Tasks'])
def list_tasks_by_filter(session: SessionDb, 
                           task_filter = FilterDepends(TaskFilter)):
    return list_tasks_by_filter_db(session,task_filter)

@router.post("/tasks/{task_id}/tags/{tag_id}",
             tags=['Tasks'])
def add_tag_to_task(task_id: int,
                    tag_id: int, session: SessionDb,
                    current_user: User = Depends(get_current_user)):
    return add_tag_to_task_bd(task_id, tag_id, session, current_user)

@router.delete("/tasks/{task_id}/tags/{tag_id}",
               tags=['Tasks'])
def delete_tag_to_task(task_id: int,
                       tag_id: int, 
                       session: SessionDb,
                       current_user: User = Depends(get_current_user)):
    return delete_tag_to_task_bd(task_id, tag_id, session, current_user)