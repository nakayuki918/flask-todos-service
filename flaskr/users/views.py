"""User views."""

from flask import Blueprint, request, jsonify
from flaskr.database import db
from .schemas import user_schemas
from .models import User
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS

app = Blueprint('user', __name__)


@app.route('/api/users')
def get_users():
    all_users = User.query.all()
    return jsonify(user_schemas.dump(all_users))


@app.route('/api/users', methods=["POST"])
def register_user():
    payload = request.json

    try:
        user = User(payload['username'], payload['email'], payload['password'])
        print(user)
        db.session.add(user)
        db.session.commit()
        return jsonify({
            'id': user.id,
            'username': user.username,
            'created_at': user.created_at,
            'update_time': user.updated_at
        }), 200

    except IntegrityError:
        print('error')
