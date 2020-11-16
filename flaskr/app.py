from flask import Flask, jsonify
from flaskr.database import init_db
from flaskr import user


def create_app():
    app = Flask(__name__)
    app.config.from_object('flaskr.config.Config')

    init_db(app)
    register_blueprints(app)

    return app


def register_blueprints(app):
    app.register_blueprint(user.views.app)


app = create_app()


@app.route('/')
def index():
    return jsonify({"language": "python"}), 200
