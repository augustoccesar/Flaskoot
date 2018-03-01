class Config(object):
    ENV = None
    DEBUG = False
    TESTING = False

    MONGO_DBNAME = None
    MONGO_HOST = None
    MONGO_PORT = 27017


class ProductionConfig(Config):
    ENV = 'PRODUCTION'


class DevelopmentConfig(Config):
    ENV = 'DEVELOPMENT'
    DEBUG = True

    MONGO_DBNAME = 'flaskoot_dev'
    MONGO_HOST = 'localhost'

    JOBS = [
        {
            'id': 'timer_job',
            'func': 'lib.api.schedules.jobs.timer_job:handle',
            'trigger': 'interval',
            'seconds': 10
        }
    ]


class TestConfig(Config):
    ENV = 'TEST'
    TESTING = True

    MONGO_DBNAME = 'flaskoot_test'
    MONGO_HOST = 'localhost'
