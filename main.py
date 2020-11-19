import uvicorn

from api.http_application import Application
from constants import Constants
from utilities.mongodb import DataStore

if __name__ == '__main__':
    DataStore().initialize()
    uvicorn.run(Application(), host=Constants.URL, port=Constants.PORT)
