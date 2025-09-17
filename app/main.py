# Punto de entrada (FastAPI app)
from fastapi import FastAPI
import jwt
from app.db.db import create_all_tables
from app.crud.user import router as user_router
from app.crud.tag import router as tag_router

encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
print("Clave hash: ", encoded_jwt)

app = FastAPI(lifespan=create_all_tables)

app.include_router(user_router)
app.include_router(tag_router)

    