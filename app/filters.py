from typing import Optional
from fastapi_filter.contrib.sqlalchemy import Filter
from app.models.task import Task

class TaskFilter(Filter):
    priority__gte: Optional[int] = None   # priority >=
    priority__lte: Optional[int] = None   # priority <=
    is_completed: Optional[bool] = None
    user_id: Optional[int] = None
    
    class Constants(Filter.Constants):
        model = Task