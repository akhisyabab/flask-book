from flask import Flask, g, jsonify
from flask_restful import Resource, reqparse
from app.models import User
from app import app, db
from datetime import datetime, timedelta
from flask_login import login_user, current_user
from .Token import *

class ApiLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        args = parser.parse_args()

        email = args['email']
        password = args['password']

        try:
            user = User.query.filter_by(email=email).first()
            if user is not None and user.is_correct_password(password):
                user.last_logged_in = user.current_logged_in
                user.current_logged_in = datetime.now()
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                token = create_token(user)
                login_user(user)
                return {'Message': 'Login berhasil', 'token': token}
            else:
                return {'Message': 'Login gagal'}
        except Exception as e:
            return {'error': str(e)}
