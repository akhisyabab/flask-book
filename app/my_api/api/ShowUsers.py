from flask import jsonify
from flask_restful import Resource
from app.models import User

class ShowUsers(Resource):
    def get(self):
        all_user = User.query.all()
        all_user_list = []
        for list in all_user :
            all_user_list.append({
                'Id':   list.id,
                'Username': list.username,
                'Confirmed ? ': list.email_confirmed
            })
        return jsonify({"result": all_user_list})
