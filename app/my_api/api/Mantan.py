from flask import jsonify, session, g
from flask_restful import Resource, reqparse
from app.models import Mantan, User
from functools import wraps
from flask_login import login_user, current_user, login_required, logout_user
from .Token import *
from app.my_api.api.Login import ApiLogin
from app import db


class ShowMantans(Resource):
    #method_decorators = [login_required]
    def get(self):
        if current_user.is_authenticated:
            all_user_mantan = Mantan.query.filter_by(user_id=current_user.id)
            all_user_mantan_list = []
            for list in all_user_mantan :
                all_user_mantan_list.append({
                    'Id': list.id,
                    'Nama': list.nama_mantan
                })
            return jsonify({"result": all_user_mantan_list})
        else:
            all_user_mantan = Mantan.query.all()
            all_user_mantan_list = []
            for list in all_user_mantan :
                all_user_mantan_list.append({
                    'Id': list.id,
                    'Nama': list.nama_mantan
                })
            return jsonify({"result": all_user_mantan_list})

class ShowMantan(Resource):
    #@login_required
    def get(self, mantanId):
        #detail_mantan = Mantan.query.filter_by(user_id=current_user.id)
        detail_mantan = Mantan.query.filter_by(id=mantanId)
       #detail_mantan_punya =  Mantan.query.filter_by(detail_mantan.Mantan.user_id == current_user.id)
        detail_mantan_list = []
        for list in detail_mantan :
            detail_mantan_list.append({
                'Id': list.id,
                'nama': list.nama_mantan,
                'Alasan Putus': list.alasan_putus
            })
        return jsonify({"result": detail_mantan_list})
    


class EditMantan(Resource):
    @login_required
    def put(self, mantanId):
        data = Mantan.query.filter_by(user_id=current_user.id)
        data = Mantan.query.filter_by(id=mantanId).first()
        parser = reqparse.RequestParser()
        parser.add_argument('nama', type=str)
        parser.add_argument('alasan', type=str)
        args = parser.parse_args()

        namaBaru = args['nama']
        alasanBaru = args['alasan']
        try:
            if data.user_id == current_user.id :
                data.nama_mantan = namaBaru
                data.alasan_putus= alasanBaru
                db.session.commit()
                return {'Status':'cek','Message': 'data updated'}
            else:
                return {'Status':'error','Message': 'tidak boleh'}

        except Exception as e:
            return {'error': str(e)}


class AddMantan(Resource):
    @login_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nama', type=str)
        parser.add_argument('alasan', type=str)
        args = parser.parse_args()

        nama = args['nama']
        alasan = args['alasan']

        try:
            new_mantan = Mantan(nama, alasan, current_user.id, False)
            db.session.add(new_mantan)
            db.session.commit()
            return {'StatusCode':'200','Message': 'Success'}

        except Exception as e:
            return {'error': str(e)}

class DeleteMantan(Resource):
    @login_required
    def delete(self,mantanId):
        #mantan = Mantan.query.filter_by(id=mantanId).first() #&& Mantan.query.filter_by(user_id=current_user.id).first()
        #data = db.session.query(Mantan, User).join(User).filter(Mantan.id == mantanId)
        data = Mantan.query.filter_by(id=mantanId).first()
        if data.user_id == current_user.id :
            db.session.delete(data)
            db.session.commit()
            return {'Status':'cek','Message': 'data terhapus'}
        else:
            return {'Status':'error','Message': 'tidak boleh'}


'''
class EditMantan(Resource):
    @login_required
    def put(self, mantanId):
        parser = reqparse.RequestParser()
        parser.add_argument('nama', type=str)
        parser.add_argument('alasan', type=str)
        args = parser.parse_args()

        namaBaru = args['nama']
        alasanBaru = args['alasan']

        try:
            data = Mantan.query.filter_by(user_id=current_user.id)
            data = Mantan.query.filter_by(id=mantanId).first()
            data.nama = namaBaru
            data.alasan_putus= alasanBaru
            db.session.commit()

        except Exception as e:
            return {'error': str(e)}
'''
