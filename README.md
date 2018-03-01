# Flaskoot
Base project for creating a full featured API using Flask.

## Requirements
- flask==0.12.2
- flask-marshmallow==0.7.0
- flasgger==0.8.1
- flask-socketio==2.9.4
- Flask-Caching==1.3.3
- flask-jwt-extended==3.7.1
- Flask-Limiter==1.0.1
- flask-apscheduler==1.7.1
- mongoengine==0.15.0

## Develop
Before all, be sure to have the following running:
- MongoDB

Now check if the `config.py` is all set to your environment.

After that, on the root folder of the project, run the following commands:
```
virtualenv -p python3.6 venv
source venv/bin/activate
pip install -r requirements.txt
APP_ENV=development python run.py
```