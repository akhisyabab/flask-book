from flask import Flask, render_template, session, request, redirect, url_for, Blueprint, flash
from app.models import Book, User
from .forms import *
from app import db
from flask_login import login_user, current_user, login_required, logout_user

members_blueprint = Blueprint('members', __name__, template_folder='templates')

@members_blueprint.route('/dashboard')
@login_required
def dashboard():
    if 'email' in session:
        all_user_book = Book.query.filter_by(user_id=current_user.id)
        return render_template('dashboard.html', book=all_user_book)
    else:
        return redirect(url_for('home.index'))

@members_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add_book():
    form = AddBookForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_book = Book(form.book_name.data, form.reason.data, current_user.id, False)
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('members.dashboard'))
    return render_template('add_book.html', form=form)


@members_blueprint.route('/book_delete/<book_id>')
def book_delete(book_id):
    data = db.session.query(Book, User).join(User).filter(Book.id == book_id).first()
    if data.Book.is_public:
        return render_template('book_detail.html', book=data)
    else:
        if current_user.is_authenticated and data.Book.user_id == current_user.id:
            data = Book.query.filter_by(id=book_id).first()
            db.session.delete(data)
            db.session.commit()
    return redirect(url_for('members.dashboard'))


@members_blueprint.route('/book_edit/<book_id>', methods=['GET', 'POST'])
def book_edit(book_id):
    data = db.session.query(Book, User).join(User).filter(Book.id == book_id).first()
    form = EditBookForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            if current_user.is_authenticated and data.Book.user_id == current_user.id:
                data = Book.query.filter_by(id=book_id).first()
                new_book_name = form.book_name.data
                new_reason = form.reason.data
                try:
                    data.book_name = new_book_name
                    data.reason= new_reason
                    db.session.commit()

                except Exception as e:
                    return {'error': str(e)}
            return redirect(url_for('members.dashboard'))

    return render_template('edit_book.html', form=form, book=data)


@members_blueprint.route('/book/<book_id>')
def book_details(book_id):
    book_with_user = db.session.query(Book, User).join(User).filter(Book.id == book_id).first()
    if book_with_user is not None:
        if book_with_user.Book.is_public:
            return render_template('book_detail.html', book=book_with_user)
        else:
            if current_user.is_authenticated and book_with_user.Book.user_id == current_user.id:
                return render_template('book_detail.html', book=book_with_user)
    else:
        flash('Error! Recipe does not exist.', 'error')
    return redirect(url_for('home.index'))


