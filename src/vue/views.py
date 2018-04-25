from flask import Blueprint, render_template, jsonify, request
# from flask_login import login_required, login_user, logout_user

from app import db
from .models import Todo, initialize_database


vue = Blueprint('vue', __name__)

@vue.route('/')
def index():
    return render_template('vue/index.html')


@vue.route('/example')
def example():
    message = "Hello Flask!"
    return render_template('vue/example.html', message=message)


@vue.route('/more')
def more():
    return render_template('vue/more.html')


@vue.route('/sqlalchemy')
def sqlalchemy():
    todos = []
    try:
        todos = Todo.query.order_by(Todo.pub_date.desc()).all()
    except:
        initialize_database()
    return render_template('vue/sqlalchemy.html', todos=todos)


@vue.route('/sqlalchemy/get', methods=['GET'])
def sqlalchemy_get():
    todos = Todo.query.order_by(Todo.pub_date.desc()).all()
    return jsonify(todos=[todo.get_dict() for todo in todos])


@vue.route('/sqlalchemy/new', methods=['POST'])
def sqlalchemy_new():
    if request.json:
        db.session.add(Todo(request.json['title']))
        db.session.commit()
    return jsonify(status='ok') # Oops: always ok...


@vue.route('/sqlalchemy/update', methods=['POST'])
def sqlalchemy_update():
    if request.json:
        todo = Todo.query.get(request.json['id'])
        todo.done = request.json['done']
        todo.title = request.json['title']
        db.session.commit()
    return jsonify(status='ok') # Oops: always ok...


@vue.route('/router')
def router():
    return render_template('vue/router.html')


@vue.route('/sfc')
def sfc():
    return render_template('vue/sfc.html')


@vue.route('/typescript')
def typescript():
    return render_template('vue/typescript.html')


@vue.route('/vuex')
def vuex():
    return render_template('vue/vuex.html')


@vue.route('/v0.10.3')
def v0_10_3():
    return render_template('vue/vue.js_v0.10.3.html')
