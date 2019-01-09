from flask_login import login_user, current_user, logout_user
from app import db
from flask_restful import Resource, Api, reqparse

class ApiLogout(Resource):
    def post(self):
        user = current_user
        user.authenticated = False
        db.session.add(user)
        db.session.commit()
        logout_user()
        return {'Message': 'Logout berhasil'}
