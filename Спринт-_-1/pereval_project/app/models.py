from pydantic import BaseModel, validator
from typing import List, Optional

class Pereval(BaseModel):
    beautyTitle: str
    title: str
    other_titles: List[str]  # Используем List вместо conlist
    connect: str
    coord_id: int
    level_winter: Optional[str] = None
    level_spring: Optional[str] = None
    level_summer: Optional[str] = None
    level_autumn: Optional[str] = None

    @validator('other_titles')
    def check_min_items(cls, v):
        if len(v) < 1:
            raise ValueError('Должен быть минимум 1 элемент в списке')
        return v