import pymongo
from bson import ObjectId
from pymongo import MongoClient

from patterns.singleton import singleton


class DataStore(object):
    URI = 'mongodb://127.0.0.1:27017'
    DATABASE: MongoClient = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(DataStore.URI)
        DataStore.DATABASE = client['movie-comparsion']

    @staticmethod
    def insert(collection, data):
        return DataStore.DATABASE[collection].insert_one(data)

    @staticmethod
    def getAll(collection):
        collection = DataStore.DATABASE[collection]
        return list(collection.find())

    @staticmethod
    def findById(collection, id):
        cursor = DataStore.DATABASE[collection].find({"_id": ObjectId(id)})
        return list(cursor)


# DataStore().initialize()

data1 = {

    "name": "data1",
    "rating": 5,
    "likes": 30,
    "imdbUrl": "url",
    "poster": "url",
    "timestamp": 15999999
}

# data = DataStore.getAll('movie')
# print(data)
#
# DataStore().initialize()
# DataStore().insert('movie', data1)