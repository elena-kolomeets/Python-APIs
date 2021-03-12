from flask import jsonify, Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine import DoesNotExist, FieldDoesNotExist, NotUniqueError, ValidationError

from api.errors import forbidden, wrong_value
from models.meals import Meals
from models.users import Users


class MealsApi(Resource):
    """Flask-resftul resource to manage all meal documents"""
    @jwt_required()
    def get(self) -> Response:
        """
        GET request method for retrieving all meals documents.
        JSON Web Token is required.
        """
        output = Meals.objects()
        return jsonify({'result': output})

    @jwt_required()
    def delete(self) -> Response:
        """
        DELETE request method for deleting all meal documents.
        JSON Web Token is required.
        Admin-level access is required.
        """
        is_admin = Users.objects.get(id=get_jwt_identity()).access.admin
        if is_admin:
            Meals.objects.delete()
            output = f'Successfully deleted all meals'
            return jsonify({'result': output})
        else:
            return forbidden()


class MealApi(Resource):
    """Flask-resftul resource to manage individual meal documents"""
    @jwt_required()
    def get(self, meal_id: str) -> Response:
        """
        GET request method for retrieving a certain meal document.
        JSON Web Token is required.
        """
        try:
            output = Meals.objects.get(id=meal_id)
            return jsonify({'result': output})
        except (DoesNotExist, ValidationError):
            output = f'No meal with id={meal_id}'
            return jsonify({'result': output})

    @jwt_required()
    def post(self) -> Response:
        """
        POST request method for creating a new meal document.
        JSON Web Token is required.
        Admin-level access is required.
        """
        # check if user is admin
        is_admin = Users.objects.get(id=get_jwt_identity()).access.admin
        if is_admin:
            data = request.get_json()
            try:  # validate the passed field values
                Meals(**data).validate()
            except (FieldDoesNotExist, TypeError, ValidationError):
                return wrong_value()
            try:
                new_meal = Meals(**data)
                new_meal.save()
                output = {'new_meal_id': str(new_meal.id)}
            except NotUniqueError:
                output = 'Meal with this name already exists.'
            except AttributeError:
                output = 'Could not get new meal\'s ID.'
            return jsonify({'result': output})
        else:
            return forbidden()

    @jwt_required()
    def put(self, meal_id: str) -> Response:
        """
        PUT request method for updating a meal document.
        JSON Web Token is required.
        Admin-level access is required.
        """
        is_admin = Users.objects.get(id=get_jwt_identity()).access.admin
        if is_admin:
            data = request.get_json()
            try:    # validate the passed field values
                Meals(**data).validate()
            except (FieldDoesNotExist, TypeError, ValidationError):
                return wrong_value()
            try:
                updated_meal = Meals.objects.get(id=meal_id)
                updated_meal.update(**data)
                output = f'Successfully updated meal {meal_id}'
            except (DoesNotExist, ValidationError):
                output = f'No meal with id={meal_id}'
            return jsonify({'result': output})
        else:
            return forbidden()

    @jwt_required()
    def delete(self, meal_id: str) -> Response:
        """
        DELETE request method for deleting a meal document.
        JSON Web Token is required.
        Admin-level access is required.
        """
        is_admin = Users.objects.get(id=get_jwt_identity()).access.admin
        if is_admin:
            try:
                Meals.objects.get(id=meal_id).delete()
                output = f'Successfully deleted meal {meal_id}'
                return jsonify({'result': output})
            except (DoesNotExist, ValidationError):
                output = f'No meal with id={meal_id}'
                return jsonify({'result': output})
        else:
            return forbidden()
