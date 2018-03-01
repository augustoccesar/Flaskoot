from flask import Flask

from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'simple'})


class CacheInitializer:
    def __init__(self, app: Flask):
        cache.init_app(app)
