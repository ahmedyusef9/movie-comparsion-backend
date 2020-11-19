from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')


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

#
# class Movie(BaseModel):
#
#     def __init__(self,
#                  _id=str,
#                  name=None,
#                  rating=0,
#                  likes=0,
#                  imdbUrl=None,
#                  poster=None,
#                  timestamp=None
#                  ):
#         self._id = _id
#         self.name = name
#         self.rating = rating
#         self.likes = likes
#         self.imdbUrl = imdbUrl
#         self.poster = poster
#         self.timestamp = timestamp
