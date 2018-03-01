import os

from flask import Flask
from flask_apscheduler import APScheduler


class Scheduler:
    def __init__(self, app: Flask):
        # Condition to prevent it to run twice while debugging
        # https://stackoverflow.com/questions/14874782/apscheduler-in-flask-executes-twice
        if not app.debug or os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
            scheduler = APScheduler()
            scheduler.init_app(app)
            scheduler.start()
