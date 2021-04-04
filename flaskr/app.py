from flask import Flask, jsonify
from flaskr.database import init_db
from flaskr import users
from flask_cors import CORS

cors = CORS()


def create_app():
    app = Flask(__name__)
    app.config.from_object('flaskr.config.Config')

    init_db(app)
    CORS(app)
    register_blueprints(app)

    return app


def register_blueprints(app):
    cors.init_app(users.views.app, supports_credentials=True, resources={r"/*": {"origins": "*"}})
    app.register_blueprint(users.views.app)


app = create_app()
