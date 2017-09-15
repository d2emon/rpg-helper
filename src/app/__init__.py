# from flask import Flask, render_template
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cache import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from config import app_config


import logging
from logging.handlers import RotatingFileHandler


def create_logger(log_config=dict()):
    handler = RotatingFileHandler(
        log_config.get("FILENAME"),
        maxBytes=log_config.get("MAX_BYTES"),
        backupCount=log_config.get("BACKUP_COUNT"),
    )
    formatter = logging.Formatter(log_config.get("FORMAT"))
    handler.setFormatter(formatter)
    return handler


def create_app(debug=False, config_name='production'):
    app = Flask(__name__, instance_relative_config=True)

    # Loading config
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    # app.config.from_envvar('FLASK_CONFIG_FILE')
    app.static_folder = app.config.get('STATIC_FOLDER', 'static')
    app.template_folder = app.config.get('TEMPLATE_FOLDER', 'templates')

    log_config = app.config.get("LOG", dict())
    app.logger.addHandler(create_logger(log_config))
    # logger = logging.getLogger('game')
    # mud_logger = logging.getLogger('mud')

    # from execom import models

    return app


import os


debug = os.environ.get('FLASK_DEBUG', False)
config_name = os.environ.get('FLASK_CONFIG', 'production')
app = create_app(config_name=config_name)

bootstrap = Bootstrap(app)

cache = Cache(app)

toolbar = DebugToolbarExtension(app)

login_manager = LoginManager(app)
# login_manager.login_message = "You must be logged in to access this page."
# login_manager.login_view = "auth.login"
login_manager.login_view = 'login'

manager = Manager(app)

db = SQLAlchemy(app)
db.create_all()

migrate = Migrate(app, db)

# Session(app)


from auth import models


# from .admin import admin as admin_blueprint
# app.register_blueprint(admin_blueprint, url_prefix='/admin')

# from .home import home as home_blueprint
# app.register_blueprint(home_blueprint)

from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)


from app.views import *
# from blog.views import *


from auth.commands import manager as auth_manager
manager.add_command("user", auth_manager)
