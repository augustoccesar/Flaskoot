from flask import Flask
from flask_marshmallow import Marshmallow

marshmallow = Marshmallow()


class MarshmallowInitializer:
    def __init__(self, app: Flask):
        marshmallow.init_app(app)
