# Punto de entrada (FastAPI app)
from fastapi import FastAPI
from app.db.db import create_all_tables
from app.crud.user import router as user_router

app = FastAPI(lifespan=create_all_tables)

app.include_router(user_router)

    