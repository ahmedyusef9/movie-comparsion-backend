import time
from datetime import datetime
from typing import List

from fastapi import FastAPI
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware

from models.movie import Movie
from utilities.mongodb import DataStore


origins = [
    "http://localhost:4200",
]

class MovieHttpApi(FastAPI):

    def __init__(self):
        super().__init__(debug=True)
        self.add_middleware(CORSMiddleware, allow_origins=origins)
        self.add_api_route('/movie', self.get, methods=['GET'], response_model=List[Movie])
        self.add_api_route('/movie', self.post, methods=['POST'], response_model=Movie)

    def get(self):
        elements = []
        for elem in DataStore.getAll('movie'):
            elements.append(Movie(**elem))
        return elements

    def post(self, movie: Movie):
        if hasattr(movie, 'id'):
            delattr(movie, 'id')
        movie.timestamp = time.time()
        ret = DataStore.insert('movie', movie.dict(by_alias=True))
        return DataStore.findById('movie', ret.inserted_id)[0]


