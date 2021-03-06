from flask import jsonify, Response


def unauthorized() -> Response:
    output = {'error': {'msg': 'Invalid email or password.'}}
    resp = jsonify({'result': output})
    resp.status_code = 401
    return resp


def forbidden() -> Response:
    output = {'error': {'msg': 'Unauthorized action.'}}
    resp = jsonify({'result': output})
    resp.status_code = 403
    return resp
