from flask import Flask
from app.database import init_db
from app import user


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    init_db(app)
    register_blueprints(app)

    return app


def register_blueprints(app):
    app.register_blueprint(user.views.app)


app = create_app()


@app.route('/')
def func_1():
    return 'Hello world'
