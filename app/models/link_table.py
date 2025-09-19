from sqlmodel import Field, SQLModel

class TaskTagLink(SQLModel, table=True):
    task_id: int | None = Field(default=None, foreign_key="task.id", primary_key=True)
    tag_id: int | None = Field(default=None, foreign_key="tag.id", primary_key=True)