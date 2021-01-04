import secrets
import time
from hashlib import md5

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.http_movie import origins
from models.user import User
from utilities.mongodb import DataStore


class UserHttpApi(FastAPI):

    def __init__(self):
        super().__init__(debug=True)
        self.add_middleware(CORSMiddleware, allow_origins=origins)
        self.add_api_route('/user', self.post, methods=['POST'], response_model=User)

    def post(self, user: User):
        if hasattr(user, 'id'):
            delattr(user, 'id')
            password = md5((user.email + user.password).encode())
        user.password = password.hexdigest()
        ret = DataStore.findUser('user', user.email, user.password)
        if not len(ret):
            # new User
            user.token = secrets.token_hex(16)
            user.timestamp = time.time()
            ret = DataStore.insert('user', user.dict(by_alias=True))
            ret = DataStore.findById('user', ret.inserted_id)
            user = User(**ret[0])
        else:
            user = User(**ret[0])

        if hasattr(user, 'password'):
            delattr(user, 'password')

        return user
