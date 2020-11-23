from flaskr.database import ma
from .models import User


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    name = ma.auto_field()


user_schema = UserSchema()
user_schemas = UserSchema(many=True)
