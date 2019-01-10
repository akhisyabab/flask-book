from flask import Flask, render_template, Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import jsonify
from flask_restful import Resource, Api, reqparse

from app import app
from app import db
app.config.from_object('config')
api = Api(app)


api_blueprint = Blueprint('api', __name__, template_folder='templates')


from app.models import User
from app.my_api.api.ShowUsers import ShowUsers
from app.my_api.api.ShowUser import ShowUser
from app.my_api.api.Register import ApiRegister
from app.my_api.api.Login import ApiLogin
from app.my_api.api.Logout import ApiLogout
from app.my_api.api.Book import ShowBooks
from app.my_api.api.Book import ShowBook
from app.my_api.api.Book import EditBook
from app.my_api.api.Book import AddBook
from app.my_api.api.Book import DeleteBook


@api_blueprint.route('/api')
def index():
    all_user= User.query.all()
    return render_template('api.html', users=all_user)


api.add_resource(ShowUsers, '/ApiShowUsers')
api.add_resource(ShowUser, '/ApiShowUser/<userId>')
api.add_resource(ApiRegister, '/ApiRegister')
api.add_resource(ApiLogin, '/ApiLogin')
api.add_resource(ApiLogout, '/ApiLogout')
api.add_resource(ShowBooks, '/ApiShowBooks')
api.add_resource(ShowBook, '/ApiShowBook/<bookId>')
api.add_resource(EditBook, '/ApiEditBook/<bookId>')
api.add_resource(AddBook, '/ApiAddBook')
api.add_resource(DeleteBook, '/ApiDeleteBook/<bookId>')

