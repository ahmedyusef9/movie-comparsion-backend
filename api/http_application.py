from fastapi import FastAPI
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from api.errors.http_error import http_error_handler
from api.http_movie import MovieHttpApi
from api.http_user import UserHttpApi

origins = [
    "http://localhost:4200",
]


class Application(FastAPI):

    def __init__(self):
        super(Application, self).__init__(debug=True)
        self.add_middleware(
            CORSMiddleware,
            # allow_origins=origins
            allow_origins=['*'],
            allow_methods=["*"],
            allow_headers=["*"]
        )
        self.routes.extend(MovieHttpApi().routes)
        self.routes.extend(UserHttpApi().routes)
        # self.add_event_handler(HTTPException, http_error_handler)
