from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel
from app.models.link_table import TaskTagLink

if TYPE_CHECKING:
    from app.models.task import Task

class TagBase(SQLModel):
    name: str = Field(default=None)
    
class CreateTag(TagBase):
    pass

class Tag(TagBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tasks: list["Task"] = Relationship(back_populates="tags", link_model=TaskTagLink)