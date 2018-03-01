from flask import Flask, make_response, jsonify


class ErrorHandlersInitializer:
    def __init__(self, app: Flask):
        @app.errorhandler(429)
        def ratelimit_handler(e):
            response = {
                'error': 'Ratelimit exceeded {}'.format(e.description)
            }
            return jsonify(response), 429
