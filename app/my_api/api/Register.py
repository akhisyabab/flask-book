from flask import Flask, url_for, render_template
from flask_restful import Resource, reqparse
from app.models import User
from app import app, db, mail
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
from threading import Thread



def send_async_email(msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, recipients, html_body):
    msg = Message(subject, recipients=recipients)
    msg.html = html_body
    thr = Thread(target=send_async_email, args=[msg])
    thr.start()

def send_confirmation_email(user_email):
    confirm_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

    confirm_url = url_for(
        'users.confirm_email',
        token=confirm_serializer.dumps(user_email, salt='email-confirmation-salt'),
        _external=True)

    html = render_template(
        'email_confirmation.html',
        confirm_url=confirm_url)

    send_email('Confirm Your Email Address', [user_email], html)



class ApiRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        args = parser.parse_args()

        email = args['email']
        password = args['password']
        try:
            new_user = User(email, password)
            db.session.add(new_user)
            db.session.commit()
            send_confirmation_email(new_user.email)
            return {'StatusCode':'200','Message': 'Cek email Konfirmasi'}

        except Exception as e:
            return {'error': str(e)}
