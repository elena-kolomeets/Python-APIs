from flask import jsonify
from flask_restful import Resource

from models.meals import Meals


class MealsApi(Resource):
    def get(self):
        result = Meals.objects()
        return jsonify({'result': result})
