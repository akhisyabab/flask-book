from flask import jsonify
from flask_restful import Resource
from app.models import User

class ShowUser(Resource):
    def get(self, userId):
        all_user = User.query.filter_by(id=userId)
        all_user_list = []
        for list in all_user :
            all_user_list.append({
                'username': list.username,
                'email': list.email,
                'registered': list.registered_on
            })
        return jsonify({"result": all_user_list})
