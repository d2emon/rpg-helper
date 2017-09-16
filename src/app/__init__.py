# from flask import Flask, render_template
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cache import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_logging import RotatingFileLogging
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from config import app_config


import os

debug = os.environ.get('FLASK_DEBUG', False)
config_name = os.environ.get('FLASK_CONFIG', 'production')


def create_app(debug=False, config_name='production'):
    app = Flask(__name__, instance_relative_config=True)

    # Loading config
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    # app.config.from_envvar('FLASK_CONFIG_FILE')
    app.static_folder = app.config.get('STATIC_FOLDER', 'static')
    app.template_folder = app.config.get('TEMPLATE_FOLDER', 'templates')
    return app


app = create_app(config_name=config_name)

# Loading modules
bootstrap = Bootstrap(app)

cache = Cache(app)

toolbar = DebugToolbarExtension(app)

logging = RotatingFileLogging(app)

login_manager = LoginManager(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "auth.login"

manager = Manager(app)

db = SQLAlchemy(app)
db.create_all()

migrate = Migrate(app, db)

# Session(app)

# Importing blueprints
from home import *
from auth import *
# from .admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(auth_blueprint)
# app.register_blueprint(admin_blueprint, url_prefix='/admin')

from rpg import *
from campaign import *
from gamesession import *

app.register_blueprint(rpg_blueprint, url_prefix='/rpg')
app.register_blueprint(campaign_blueprint, url_prefix='/campaign')
app.register_blueprint(session_blueprint, url_prefix='/session')

from pathfinder import *
from gurps import *
from tnt import *

app.register_blueprint(pathfinder_blueprint, url_prefix='/pathfinder')
app.register_blueprint(gurps_blueprint, url_prefix='/gurps')
app.register_blueprint(tnt_blueprint, url_prefix='/tnt')


from app.views import *

# Adding commands from managers
from auth.commands import manager as auth_manager
manager.add_command("user", auth_manager)