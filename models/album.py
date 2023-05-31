from models.base import BaseModel


class Album(BaseModel):
    id: str
    name: str
    release_date: str
    total_tracks: int
