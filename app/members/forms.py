from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, Length, EqualTo, Email

class AddBookForm(FlaskForm):
    book_name = StringField('Book Name', validators=[DataRequired()])
    reason = StringField('Recipe Description', validators=[DataRequired()])


class Book_name_changeForm(FlaskForm):
    book_name = StringField('Book Name', validators=[DataRequired()])


class EditBookForm(FlaskForm):
    book_name = StringField('Book Name', validators=[DataRequired()])
    reason = StringField('Reason ', validators=[DataRequired()])
