from flask import jsonify, Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine import DoesNotExist, FieldDoesNotExist, NotUniqueError, ValidationError

from api.errors import forbidden, wrong_value
from models.users import Users


class UsersApi(Resource):
    """Flask-resftul resource to manage db.users collection"""
    @jwt_required()
    def get(self) -> Response:
        """
        GET request method for retrieving all user documents.
        JSON Web Token is required.
        Admin-level access is required.
        """
        is_admin = Users.objects.get(id=get_jwt_identity()).access.admin
        if is_admin:
            output = Users.objects.exclude('password')
            return jsonify({'result': output})
        else:
            return forbidden()

    @jwt_required()
    def delete(self) -> Response:
        """
        DELETE request method for deleting all user documents.
        JSON Web Token is required.
        Admin-level access is required.
        """
        is_admin = Users.objects.get(id=get_jwt_identity()).access.admin
        if is_admin:
            Users.objects.delete()
            output = f'Successfully deleted all users'
            return jsonify({'result': output})
        else:
            return forbidden()


class UserApi(Resource):
    """Flask-resftul resource to manage individual user documents"""
    @jwt_required()
    def get(self, user_id: str) -> Response:
        """
        GET request method for retrieving a certain user document.
        JSON Web Token is required.
        Admin-level access is required or logged in user should be the requested user.
        """
        is_admin = Users.objects.get(id=get_jwt_identity()).access.admin
        # check if requested user is the same as logged in user
        is_logged_in_user = get_jwt_identity() == user_id
        if is_admin or is_logged_in_user:
            try:
                output = Users.objects.exclude('password').get(id=user_id)
                return jsonify({'result': output})
            except (DoesNotExist, ValidationError):
                output = f'No user with id={user_id}'
                return jsonify({'result': output})
        else:
            return forbidden()

    @jwt_required()
    def post(self) -> Response:
        pass

    @jwt_required()
    def put(self) -> Response:
        pass

    @jwt_required()
    def delete(self) -> Response:
        pass
