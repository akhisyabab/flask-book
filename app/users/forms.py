from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, Length, EqualTo, Email


class punyaku(FlaskForm):
    username = StringField('username', [validators.Length(min=4, max=25)])
    password = StringField('password', [validators.Length(min=4, max=25)])


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password', validators=[DataRequired()])

class EmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])

class UsernameForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])

class PasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
