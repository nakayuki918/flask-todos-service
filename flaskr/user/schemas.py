from flaskr.database import ma
from flask_marshmallow.fields import fields
from .models import User


class UserSchema(ma.Schema):
    class Meta:
        model = User

    name = fields.Str()
    created_at = fields.DateTime('%Y-%m-%dT%H:%M:%S+09:00')
    updated_at = fields.DateTime('%Y-%m-%dT%H:%M:%S+09:00')


user_schema = UserSchema()
user_schemas = UserSchema(many=True)
