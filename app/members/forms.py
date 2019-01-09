from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, Length, EqualTo, Email

class AddMantanForm(FlaskForm):
    nama_mantan = StringField('Nama Mantan', validators=[DataRequired()])
    alasan_putus = StringField('Recipe Description', validators=[DataRequired()])


class nama_mantan_changeForm(FlaskForm):
    nama_mantan = StringField('Nama Mantan', validators=[DataRequired()])


class EditMantanForm(FlaskForm):
    nama_mantan = StringField('Nama Mantan', validators=[DataRequired()])
    alasan_putus = StringField('Alasan Putus', validators=[DataRequired()])
