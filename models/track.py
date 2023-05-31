from models.album import Album
from models.base import BaseModel


class Track(BaseModel):
    id: str
    name: str
    album: Album
