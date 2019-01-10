from flask import jsonify, session, g
from flask_restful import Resource, reqparse
from app.models import Book, User
from functools import wraps
from flask_login import login_user, current_user, login_required, logout_user
from .Token import *
from app.my_api.api.Login import ApiLogin
from app import db


class ShowBooks(Resource):
    #method_decorators = [login_required]
    def get(self):
        if current_user.is_authenticated:
            all_user_book = Book.query.filter_by(user_id=current_user.id)
            all_user_book_list = []
            for list in all_user_book :
                all_user_book_list.append({
                    'Id': list.id,
                    'Name': list.book_name
                })
            return jsonify({"result": all_user_book_list})
        else:
            all_user_book = Book.query.all()
            all_user_book_list = []
            for list in all_user_book :
                all_user_book_list.append({
                    'Id': list.id,
                    'name': list.book_name
                })
            return jsonify({"result": all_user_book_list})

class ShowBook(Resource):
    #@login_required
    def get(self, bookId):
        #detail_book = Book.query.filter_by(user_id=current_user.id)
        detail_book = Book.query.filter_by(id=bookId)
       #detail_book_punya =  Book.query.filter_by(detail_book.Book.user_id == current_user.id)
        detail_book_list = []
        for list in detail_book :
            detail_book_list.append({
                'Id': list.id,
                'Name': list.book_name,
                'Reason': list.reason
            })
        return jsonify({"result": detail_book_list})
    


class EditBook(Resource):
    @login_required
    def put(self, bookId):
        data = Book.query.filter_by(user_id=current_user.id)
        data = Book.query.filter_by(id=bookId).first()
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('reason', type=str)
        args = parser.parse_args()

        new_name = args['name']
        new_reason = args['reason']
        try:
            if data.user_id == current_user.id :
                data.book_name = new_name
                data.reason= new_reason
                db.session.commit()
                return {'Status':'cek','Message': 'data updated'}
            else:
                return {'Status':'error','Message': 'tidak boleh'}

        except Exception as e:
            return {'error': str(e)}


class AddBook(Resource):
    @login_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('reason', type=str)
        args = parser.parse_args()

        name = args['name']
        reason = args['reason']

        try:
            new_book = Book(name, reason, current_user.id, False)
            db.session.add(new_book)
            db.session.commit()
            return {'StatusCode':'200','Message': 'Success'}

        except Exception as e:
            return {'error': str(e)}

class DeleteBook(Resource):
    @login_required
    def delete(self,bookId):
        #book = Book.query.filter_by(id=bookId).first() #&& Book.query.filter_by(user_id=current_user.id).first()
        #data = db.session.query(Book, User).join(User).filter(Book.id == bookId)
        data = Book.query.filter_by(id=bookId).first()
        if data.user_id == current_user.id :
            db.session.delete(data)
            db.session.commit()
            return {'Status':'cek','Message': 'data terhapus'}
        else:
            return {'Status':'error','Message': 'tidak boleh'}

