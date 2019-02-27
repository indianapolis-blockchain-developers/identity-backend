import os

from flask import Flask
from flask_restful import Api

from identity_app.resources.ping import Ping
from identity_app.resources.user import UserV1
from identity_app.db import db


POSTGRES_URL = os.getenv("POSTGRES_URL")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PW = os.getenv("POSTGRES_PW")
POSTGRES_DB = os.getenv("POSTGRES_DB")
DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['PROPOGATE_EXCEPTIONS'] = True
app.secret_key = os.getenv('APP_SECRET')


api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


# API definitions
api.add_resource(Ping, '/')
api.add_resource(UserV1, '/api/v1/users', '/api/v1/users/<int:id>')
