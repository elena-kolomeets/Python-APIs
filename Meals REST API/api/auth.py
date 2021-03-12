import datetime

from flask import jsonify, Response, request
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource
from mongoengine import DoesNotExist, NotUniqueError, ValidationError, FieldDoesNotExist

from models.users import Users
from api.errors import unauthorized, wrong_value


class SignUpApi(Resource):
    """Flask-resftul resource for creating new user."""
    @staticmethod
    def post() -> Response:
        """POST request method for creating user."""
        data = request.get_json()
        try:  # validate the passed field values
            Users(**data).validate()
        except (FieldDoesNotExist, TypeError, ValidationError):
            return wrong_value()
        try:
            new_user = Users(**data)
            new_user.save()
            output = {'new_user_id': str(new_user.id)}
        except NotUniqueError:
            output = 'User with this email already exists.'
        except AttributeError:
            output = 'Could not get new user\'s ID.'
        return jsonify({'result': output})


class LogInApi(Resource):
    """Flask-resftul resource for retrieving user web token."""
    @staticmethod
    def post() -> Response:
        """POST request method for retrieving user web token.."""
        data = request.get_json()
        try:
            Users(**data).validate()
            user = Users.objects.get(email=data.get('email'))
            correct_pwd = user.check_pwd_hash(data.get('password'))
            if correct_pwd:
                expires = datetime.timedelta(days=5)
                access_token = create_access_token(identity=str(user.id), expires_delta=expires)
                refresh_token = create_refresh_token(identity=str(user.id))
                output = {'access_token': access_token,
                          'user_id': str(user.id),
                          'refresh_token': refresh_token}
                return jsonify({'result': output})
            else:
                return unauthorized()
        except DoesNotExist:
            return unauthorized()
        except (FieldDoesNotExist, TypeError, ValidationError):
            return wrong_value()
