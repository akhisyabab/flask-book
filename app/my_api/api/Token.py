from flask import Flask, g, jsonify, request, redirect, url_for
from datetime import datetime, timedelta
from flask_jwt import jwt
from config import SECRET_KEY;
from functools import wraps

def create_token(user):
    payload = {
        'sub': user.id,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(days=1),
        'scope': user.role
    }
    token = jwt.encode(payload, SECRET_KEY)
    return token.decode('unicode_escape')


def parse_token(req):

    token = req.headers.get('Authorization').split()[1]
    return jwt.decode(token, SECRET_KEY, algorithms='HS256')

'''

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.headers.get('Authorization'):
            response = jsonify(message='Missing authorization header')
            response.status_code = 401
            return response

        try:
            payload = parse_token(request)
        except Exception as e:
            return {'error': str(e)}
        g.user_id = payload['sub']

        return f(*args, **kwargs)
'''
