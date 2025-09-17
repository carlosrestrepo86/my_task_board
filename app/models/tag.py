from sqlmodel import Field, SQLModel

class TagBase(SQLModel):
    name: str = Field(default=None)
    
class CreateTag(TagBase):
    pass

class Tag(TagBase, table=True):
    id: int | None = Field(default=None, primary_key=True)