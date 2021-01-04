from typing import Optional

from bson import ObjectId
from pydantic import Field
from pydantic.main import BaseModel

from models.pyObjectId import PyObjectId


class User(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    firstName: str = None
    lastName: str = None
    email: str = None
    password: str = None
    userLvl: str = None
    movieLikes = []
    token: str = None
    timestamp: float = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }