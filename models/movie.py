from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from models.pyObjectId import PyObjectId


class Movie(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    name: str = None
    rating: float = 0
    likes: float = 0
    imdbUrl: str = None
    poster: str = None
    timestamp: float = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
