import os
from lib.app import app

HOST = '0.0.0.0'
PORT = os.environ.get('PORT', 5000)

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
