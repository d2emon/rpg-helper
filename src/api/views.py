from flask import Blueprint, jsonify, request, flash, get_flashed_messages
# from flask import Blueprint, render_template, redirect, flash, url_for
# from flask_login import login_required, login_user, logout_user
from app import app, db
from blueprints.auth.models import User
# from vue.models import Todo
# from .forms import LoginForm, RegisterForm

from datetime import datetime, timedelta

import jwt

api = Blueprint('api', __name__)


@api.route('/', methods=['GET'])
def index():
    """
    Main API page
    """
    return jsonify(status='ok')


@api.route('/messages', methods=['GET'])
def messages():
    """
    List Messages
    """
    flash("Test message", "warning")
    return jsonify(get_flashed_messages(with_categories=True))


@api.route('/users', methods=['GET'])
def users():
    """
    List Users
    """
    return jsonify([user.as_dict for user in User.query.all()])


@api.route('/register', methods=['POST'])
def add_user():
    """
    New User
    """
    data = request.get_json()
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify({
        'user': user.as_dict,
        'message': 'You have successfully registered! You may now login.',
        'status': 'ok',
    }), 201


@api.route('/login', methods=['POST'])
def login():
    """
    Login User
    """
    data = request.get_json()
    user = User.authenticate(**data)
    # user = User.login(**data)
    print(data)
    print(user)

    if not user:
        flash('Invalid email or password')
        return jsonify({
            'message': 'Invalid credentials',
            'authenticated': False
        }), 401

    token = jwt.encode({
        'sub': user.username,
        'iat':datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }, app.config['SECRET_KEY'])
    return jsonify({ 'token': token.decode('UTF-8') })


@api.route('/todo/get', methods=['GET'])
def sqlalchemy_get():
    todos = [] # Todo.query.order_by(Todo.pub_date.desc()).all()
    return jsonify(todos=[todo.get_dict() for todo in todos])


@api.route('/todo/new', methods=['POST'])
def sqlalchemy_new():
    if request.json:
        # db.session.add(Todo(request.json['title']))
        db.session.commit()
    return jsonify(status='ok') # Oops: always ok...


@api.route('/todo/update', methods=['POST'])
def sqlalchemy_update():
    if request.json:
        # todo = Todo.query.get(request.json['id'])
        # todo.done = request.json['done']
        # todo.title = request.json['title']
        db.session.commit()
    return jsonify(status='ok') # Oops: always ok...
