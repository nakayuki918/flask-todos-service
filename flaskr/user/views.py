"""User views."""

from flask import Blueprint
# from flaskr.database import db
from .schemas import user_schemas
from .models import User

app = Blueprint('user', __name__)


@app.route('/api/user')
def get_user():
    all_users = User.
    return user_schemas.dump(all_users)
