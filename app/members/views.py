# app/users/views.py


#################
#### imports ####
#################


from flask import Flask, render_template, session, request, redirect, url_for, Blueprint, flash
from app.models import Mantan, User
from .forms import *
from app import db
from flask_login import login_user, current_user, login_required, logout_user
#import sqlite3 as sql

################
#### config ####
################

members_blueprint = Blueprint('members', __name__, template_folder='templates')



################
#### routes ####
################

@members_blueprint.route('/dashboard')
@login_required
def dashboard():
    if 'email' in session:
        all_user_mantan = Mantan.query.filter_by(user_id=current_user.id)
        return render_template('dashboard.html', mantan=all_user_mantan)
    #    email=session['email']
    #   all_public_mantan = Mantan.query.filter_by(is_public=True)
    #    return render_template('sashboard.html', public_recipes=all_public_mantan)
    #   all_mantan = Mantan.query.all()
    #   return render_template('dashboard.html', mantan=all_mantan)
    else:
        return redirect(url_for('home.index'))

@members_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def tambah_mantan():
    form = AddMantanForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_mantan = Mantan(form.nama_mantan.data, form.alasan_putus.data, current_user.id, False)
            db.session.add(new_mantan)
            db.session.commit()
            return redirect(url_for('members.dashboard'))
    return render_template('tambah_mantan.html', form=form)


@members_blueprint.route('/mantan_delete/<mantan_id>')
def mantan_delete(mantan_id):
    data = db.session.query(Mantan, User).join(User).filter(Mantan.id == mantan_id).first()
    if data.Mantan.is_public:
        return render_template('mantan_detail.html', mantan=data)
    else:
        if current_user.is_authenticated and data.Mantan.user_id == current_user.id:
            data = Mantan.query.filter_by(id=mantan_id).first()
            db.session.delete(data)
            db.session.commit()
    return redirect(url_for('members.dashboard'))



@members_blueprint.route('/mantan_edit/<mantan_id>', methods=['GET', 'POST'])
def mantan_edit(mantan_id):
    data = db.session.query(Mantan, User).join(User).filter(Mantan.id == mantan_id).first()
    form = EditMantanForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            if current_user.is_authenticated and data.Mantan.user_id == current_user.id:
                data = Mantan.query.filter_by(id=mantan_id).first()
                new_nama_mantan = form.nama_mantan.data
                new_alasan_putus = form.alasan_putus.data
                try:
                    data.nama_mantan = new_nama_mantan
                    data.alasan_putus= new_alasan_putus
                    db.session.commit()

                except Exception as e:
                    return {'error': str(e)}
            return redirect(url_for('members.dashboard'))

    return render_template('edit_mantan.html', form=form, mantan=data)





@members_blueprint.route('/mantan/<mantan_id>')
def mantan_details(mantan_id):
    mantan_with_user = db.session.query(Mantan, User).join(User).filter(Mantan.id == mantan_id).first()
    if mantan_with_user is not None:
        if mantan_with_user.Mantan.is_public:
            return render_template('mantan_detail.html', mantan=mantan_with_user)
        else:
            if current_user.is_authenticated and mantan_with_user.Mantan.user_id == current_user.id:
                return render_template('mantan_detail.html', mantan=mantan_with_user)
            #else:
            #    flash('Error! Incorrect permissions to access this mantan.', 'error')
    else:
        flash('Error! Recipe does not exist.', 'error')
    return redirect(url_for('home.index'))


'''
@members_blueprint.route('/nama_mantan_change/<mantan_id>', methods=["GET", "POST"])
def nama_mantan_change(mantan_id):

    form = nama_mantan_changeForm()
    if request.method == 'POST':
        if form.validate_on_submit():
                nama_mantan = current_user
                user.username = form.username.data
                db.session.add(user)
                db.session.commit()
                flash('Username Changed', 'success')
                return redirect(url_for('users.user_profile'))
        else:
            flash('Sorry, that username already exists!', 'error')
            return redirect(url_for('users.user_profile'))
    return render_template('username_change.html', form=form)

'''

#cara menggunakan routes#
'''

from . import users

@base.route('/')
def index():
	return render_template('blueprint.html')


@users.route('/login', methods=('GET', 'POST'))
def login():
    form = punyaku()
    if request.method == 'POST':
        if form.validate_on_submit():
            session['username'] = request.form['username']
            if request.form['username'] == 'akhi' and request.form['password'] == '1234':
                return redirect(url_for('dashboard'))
            return "username atau password salah"
        return "gagal valid"
    return render_template('login.html', form=form)
'''
