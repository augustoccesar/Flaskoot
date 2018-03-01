import os

from flask import Flask
from flasgger import Swagger

from lib.api.utils.marshmallow import MarshmallowInitializer
from lib.api.utils.limiter import LimiterInitializer
from lib.api.utils.cache import CacheInitializer
from lib.api.utils.error_handlers import ErrorHandlersInitializer

from lib.api.models.mongo import MongoDBInitializer
from lib.api.router import Router
from lib.api.schedules.scheduler import Scheduler

env = os.environ.get('APP_ENV')

if env and env.upper() in ('PRODUCTION', 'DEVELOPMENT', 'TEST'):
    app = Flask(__name__)

    app.config.from_object('lib.config.{}Config'.format(env.capitalize()))

    MarshmallowInitializer(app)
    LimiterInitializer(app)
    CacheInitializer(app)
    MongoDBInitializer(app)
    Scheduler(app)
    
    ErrorHandlersInitializer(app)
    Router(app)

    Swagger(app)
else:
    raise AttributeError(
        'APP_ENV variable must be one of (PRODUCTION, DEVELOPMENT, TEST)')
