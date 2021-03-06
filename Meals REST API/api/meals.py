from flask import jsonify, Response
from flask_restful import Resource

from models.meals import Meals


class MealsApi(Resource):
    @staticmethod
    def get(self) -> Response:
        result = Meals.objects()
        return jsonify({'result': result})
