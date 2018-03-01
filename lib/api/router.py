from flask import Flask

from lib.api.controllers.user_controller import user_controller

class Router:
    def __init__(self, app: Flask):
        app.register_blueprint(user_controller, url_prefix='/users')
