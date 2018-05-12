from .models import *
from .views import rpg as rpg_blueprint

from temporary.pathfinder import *
from temporary.gurps import *
from temporary.tnt import *


class RpgManager(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):       
        app.register_blueprint(pathfinder_blueprint, url_prefix='/pathfinder')
        app.register_blueprint(gurps_blueprint, url_prefix='/gurps')
        app.register_blueprint(tnt_blueprint, url_prefix='/tnt')