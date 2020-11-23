"""User views."""

from flask import Blueprint, jsonify
# from flaskr.database import db
from .schemas import user_schemas
from .models import User

app = Blueprint('user', __name__)


@app.route('/api/user')
def get_users():
    all_users = User.query.all()
    return jsonify(user_schemas.dump(all_users))
