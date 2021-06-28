from flask import jsonify, Response


def unauthorized() -> Response:
    output = {'error': 'Invalid email or password.'}
    resp = jsonify({'result': output})
    resp.status_code = 401
    return resp


def forbidden() -> Response:
    output = {'error': 'Unauthorized action.'}
    resp = jsonify({'result': output})
    resp.status_code = 403
    return resp


def wrong_value() -> Response:
    output = {'error': 'Wrong values passed or missing required values in the request body.'}
    resp = jsonify({'result': output})
    resp.status_code = 400
    return resp


def not_admin() -> Response:
    output = {'error': 'Operation rejected: only another admin user can give users admin access.'}
    resp = jsonify({'result': output})
    resp.status_code = 401
    return resp
