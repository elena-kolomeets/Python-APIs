from flask import jsonify
from flask_restful import Resource

from models.users import Users, Access


class UsersApi(Resource):
    def get(self):
        result = Users.objects()
        return jsonify({'result': result})
