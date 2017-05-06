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
from app.my_api.api.Mantan import ShowMantans
from app.my_api.api.Mantan import ShowMantan
from app.my_api.api.Mantan import EditMantan
from app.my_api.api.Mantan import AddMantan
from app.my_api.api.Mantan import DeleteMantan


@api_blueprint.route('/api')
def index():
    all_user= User.query.all()
    return render_template('api.html', users=all_user)


# Read Data API
api.add_resource(ShowUsers, '/ApiShowUsers')
api.add_resource(ShowUser, '/ApiShowUser/<userId>')
api.add_resource(ApiRegister, '/ApiRegister')
api.add_resource(ApiLogin, '/ApiLogin')
api.add_resource(ApiLogout, '/ApiLogout')
api.add_resource(ShowMantans, '/ApiShowMantans')
api.add_resource(ShowMantan, '/ApiShowMantan/<mantanId>')
api.add_resource(EditMantan, '/ApiEditMantan/<mantanId>')
api.add_resource(AddMantan, '/ApiAddMantan')
api.add_resource(DeleteMantan, '/ApiDeleteMantan/<mantanId>')



'''@api_blueprint.route('/ShowUsers')
def ShowUsers():
    all_user = User.query.all()
    all_user_list = []
    for list in all_user :
        all_user_list.append({
            'id': list.id,
            'email': list.email,
        })
    return jsonify({"result": all_user_list})
'''
