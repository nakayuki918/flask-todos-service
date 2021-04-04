from flask import Blueprint, request, jsonify
from flaskr.database import db

app = Blueprint('articles', __name__)

@app.route('api/articles')
def get_articles():
