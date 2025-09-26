from fastapi import FastAPI
from app.db.db import create_all_tables
from app.api.users import router as user_router
from app.api.tags import router as tag_router
from app.api.tasks import router as task_router
from app.api.auth import router as auth_router

app = FastAPI(lifespan=create_all_tables)

app.include_router(user_router)
app.include_router(tag_router)
app.include_router(task_router)
app.include_router(auth_router)

    