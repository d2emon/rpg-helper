from flask import Blueprint, render_template

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
