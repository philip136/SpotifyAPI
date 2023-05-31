from typing import List
from models.base import BaseModel


class Artist(BaseModel):
    id: str
    name: str
    genres: List[str]
    followers_count: int
