import datetime

from flask import jsonify, Response, request
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource

from models.users import Users
from api.errors import unauthorized


class SignUpApi(Resource):
    """Flask-resftul resource for creating new user."""
    @staticmethod
    def post() -> Response:
        """POST response method for creating user."""
        data = request.get_json()
        new_user = Users(**data)
        new_user.save()
        output = {'new_user_id': str(new_user.id)}
        return jsonify({'result': output})


class LogInApi(Resource):
    """Flask-resftul resource for retrieving user web token."""
    @staticmethod
    def post() -> Response:
        data = request.get_json()
        user = Users.objects.get(email=data.get('email'))
        correct_pwd = user.check_pwd_hash(data.get('password'))
        if correct_pwd:
            expires = datetime.timedelta(days=5)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)
            refresh_token = create_refresh_token(identity=str(user.id))
            output = {'access_token': access_token,
                      'refresh_token': refresh_token}
        else:
            return unauthorized()
