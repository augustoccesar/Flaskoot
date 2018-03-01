from datetime import datetime

from flask import Flask
from mongoengine import connect


class MongoDBInitializer:
    def __init__(self, app: Flask):
        connect(app.config['MONGO_DBNAME'],
                host=app.config['MONGO_HOST'],
                port=app.config['MONGO_PORT'])
