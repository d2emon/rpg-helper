from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cache import Cache
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from temporary.flask_utils import FlaskUtils
from config import app_config
# from .flask_vue import FlaskVue


import os

debug = os.environ.get('FLASK_DEBUG', False)
config_name = os.environ.get('FLASK_CONFIG', 'production')


def create_app(debug=False, config_name='production'):
    app = Flask(
        __name__,
        instance_relative_config=True
    )

    # Loading config
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    # app.config.from_envvar('FLASK_CONFIG_FILE')
    return app




app = create_app(debug, config_name=config_name)


# Loading modules
class FlaskModules:
    def __init__(self, app):
        self.app = app

        self.bootstrap = Bootstrap(self.app)

        self.cache = Cache(self.app)

        self.cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

        self.utils = FlaskUtils(self.app)

        self.login_manager = LoginManager(self.app)
        self.login_manager.login_message = "You must be logged in to access this page."
        self.login_manager.login_view = "auth.login"

        self.manager = Manager(self.app)

        self.db = SQLAlchemy(self.app)
        self.db.create_all()

        self.migrate = Migrate(self.app, self.db)

        # self.session = Session(self.app)


app.modules = FlaskModules(app)

bootstrap = app.modules.bootstrap
cache = app.modules.cache
utils = app.modules.utils
login_manager = app.modules.login_manager
manager = app.modules.manager
db = app.modules.db
migrate = app.modules.migrate


from app.views import *


# Importing blueprints
from api import *
app.register_blueprint(api_blueprint, url_prefix='/api')
app.register_blueprint(world_api_blueprint, url_prefix='/api/world')
app.register_blueprint(npc_api_blueprint, url_prefix='/api/npc')


from blueprints.home import *
from blueprints.auth import *
from admin import *

app.register_blueprint(home_blueprint, url_prefix='/main')
app.register_blueprint(auth_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')

from blueprints.rpg import *
from blueprints.campaign import *
from blueprints.gamesession import *
from blueprints.world import *
from npc import *

app.register_blueprint(rpg_blueprint, url_prefix='/rpg')
app.register_blueprint(campaign_blueprint, url_prefix='/campaign')
app.register_blueprint(session_blueprint, url_prefix='/session')
app.register_blueprint(world_blueprint, url_prefix='/world')

# from temporary.vue import *
# app.register_blueprint(vue_blueprint, url_prefix='/vue')

rpg_manager = RpgManager(app)

# from app.views import *

# Adding commands from managers
from blueprints.auth.commands import manager as auth_manager
from admin.commands import manager as admin_manager
manager.add_command("user", auth_manager)
manager.add_command("admin", admin_manager)
