from flask import Flask
from app.database import init_db
import app.users.models

def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object('app.config.Config')

    init_db(flask_app)

    return flask_app


app = create_app()
