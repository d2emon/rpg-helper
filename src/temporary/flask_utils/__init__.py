from flask_debugtoolbar import DebugToolbarExtension
from flask_logging import RotatingFileLogging


# __version__ = '3.3.7.1.dev1'


class FlaskUtils(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):       
        app.static_folder = app.config.get('STATIC_FOLDER', 'static')
        app.template_folder = app.config.get('TEMPLATE_FOLDER', 'templates')

        self.logging = RotatingFileLogging(app)
        self.toolbar = DebugToolbarExtension(app)