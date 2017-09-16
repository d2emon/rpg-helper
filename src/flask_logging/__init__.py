from logging import Formatter
from logging.handlers import RotatingFileHandler

# __version__ = '3.3.7.1.dev1'


class RotatingFileLogging(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):       
        app.config.setdefault('LOG_FILENAME', "app.log")
        app.config.setdefault('LOG_MAX_BYTES', 1024 * 1024)
        app.config.setdefault('LOG_BACKUP_COUNT', 10)
        app.config.setdefault('LOG_FORMAT', "%(asctime)s[%(levelname)s]:\t%(message)s\tin %(module)s at %(lineno)d")

        app.logger.addHandler(self.create_handler(app))
        
        # logger = logging.getLogger('game')
        # mud_logger = logging.getLogger('mud')
        
    def create_handler(self, app):
        handler = RotatingFileHandler(
            app.config["LOG_FILENAME"],
            maxBytes=app.config["LOG_MAX_BYTES"],
            backupCount=app.config["LOG_BACKUP_COUNT"],
        )
        handler.setFormatter(self.create_formatter(app))
        return handler
    
    def create_formatter(self, app):
        return Formatter(app.config["LOG_FORMAT"])