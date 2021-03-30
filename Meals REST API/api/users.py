from flask import jsonify, Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine import DoesNotExist, FieldDoesNotExist, NotUniqueError, ValidationError
from pymongo.errors import OperationFailure

from api.errors import forbidden, wrong_value, not_admin
from models.users import Users, Meals


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
    def post(self) -> Response:
        """
        POST request method for creating a new user document.
        JSON Web Token is required.
        Admin-level access is required.
        """
        is_admin = Users.objects.get(id=get_jwt_identity()).access.admin
        if is_admin:
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
                output = 'User with this email already exists'
            except AttributeError:
                output = 'Could not get new user\'s ID.'
            return jsonify({'result': output})
        else:
            return forbidden()

    # @jwt_required()
    # def delete(self) -> Response:
    #     """
    #     DELETE request method for deleting all user documents.
    #     JSON Web Token is required.
    #     Admin-level access is required.
    #     """
    #     is_admin = Users.objects.get(id=get_jwt_identity()).access.admin
    #     if is_admin:
    #         Users.objects.delete()
    #         output = f'Successfully deleted all users'
    #         return jsonify({'result': output})
    #     else:
    #         return forbidden()


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
    def put(self, user_id: str) -> Response:
        """
        PUT request method for updating a certain user document.
        JSON Web Token is required.
        Admin-level access is required or logged in user should be the requested user.
        """
        is_admin = Users.objects.get(id=get_jwt_identity()).access.admin
        # check if requested user is the same as logged in user
        is_logged_in_user = get_jwt_identity() == user_id
        if is_admin or is_logged_in_user:
            data = request.get_json()
            try:  # validate the passed field values
                Users(**data).validate()
            except (FieldDoesNotExist, TypeError, ValidationError, NotUniqueError):
                return wrong_value()
            try:
                updated_user = Users.objects.get(id=user_id)
                # preventing change of email or password
                if data['email'] != updated_user.email or \
                        not updated_user.check_pwd_hash(data['password']):
                    output = 'Update rejected: change of email or password is not allowed.'
                    resp = jsonify({'result': output})
                    resp.status_code = 400
                    return resp
                # retrieve referenced Meals documents and add
                # their reference to fav_meals list (overwrites old list)
                if data.get('fav_meals') is not None:
                    try:
                        fav_meals_list = [Meals.objects.get(__raw__=meal) for meal in data['fav_meals']]
                        updated_user.update(
                            set__fav_meals=fav_meals_list)
                    except (OperationFailure, DoesNotExist, ValueError):
                        return wrong_value()
                # if new value for the field is not given, don't change it
                updated_user.update(
                    set__name=data.get('name', updated_user.name))
                # grant admin access to the user (only existing admin can do it)
                if data.get('access') is not None:
                    if data['access']['admin']:
                        if is_admin:
                            updated_user.update(
                                set__access=data.get('access', updated_user.access))
                        else:
                            return not_admin()
                output = f'Successfully updated user {user_id}'
            except (DoesNotExist, ValidationError):
                output = f'No user with id={user_id}'
            return jsonify({'result': output})
        else:
            return forbidden()

    @jwt_required()
    def delete(self, user_id: str) -> Response:
        """
        DELETE request method for deleting a certain user document.
        JSON Web Token is required.
        Admin-level access is required or logged in user should be the requested user.
        """
        is_admin = Users.objects.get(id=get_jwt_identity()).access.admin
        # check if requested user is the same as logged in user
        is_logged_in_user = get_jwt_identity() == user_id
        if is_admin or is_logged_in_user:
            try:
                Users.objects.get(id=user_id).delete()
                output = f'Successfully deleted user {user_id}'
                return jsonify({'result': output})
            except (DoesNotExist, ValidationError):
                output = f'No user with id={user_id}'
                return jsonify({'result': output})
        else:
            return forbidden()
