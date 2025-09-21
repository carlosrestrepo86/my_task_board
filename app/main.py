# Punto de entrada (FastAPI app)
from fastapi import FastAPI
from app.db.db import create_all_tables
from app.routers.user import router as user_router
from app.routers.tag import router as tag_router
from app.routers.task import router as task_router

app = FastAPI(lifespan=create_all_tables)

app.include_router(user_router)
app.include_router(tag_router)
app.include_router(task_router)

    