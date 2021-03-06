from flask import jsonify, Response
from flask_restful import Resource

from models.users import Users, Access


class UsersApi(Resource):
    @staticmethod
    def get(self) -> Response:
        result = Users.objects()
        return jsonify({'result': result})
