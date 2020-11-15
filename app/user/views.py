"""User views."""

from flask import Blueprint

app = Blueprint('user', __name__)


@app.route('/api/user')
def get_user():
    return 'user'
