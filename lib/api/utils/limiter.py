from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)


class LimiterInitializer:
    def __init__(self, app: Flask):
        limiter.init_app(app)
