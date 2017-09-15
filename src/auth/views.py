from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import login_required, login_user, logout_user
from app import db
from .models import User
from .forms import LoginForm, RegisterForm


auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """
    form = RegisterForm()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered! You may now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form, title='Register')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.by_username(form.username.data)
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(user.after_login)
        else:
            flash('Invalid email or password')
    return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    return redirect(url_for('auth.login'))
