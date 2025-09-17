from typing import Annotated
from fastapi import Depends, FastAPI
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

sqlite_name = "db.sqlite3"
sqlite_url = f"sqlite:///{sqlite_name}"

engine = create_engine(sqlite_url)

def create_all_tables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

def get_session():
    with Session(engine) as session:
        yield session

SessionDb = Annotated[Session, Depends(get_session)]