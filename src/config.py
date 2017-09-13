# import sys
import os
import locale


BASE_DIR = os.path.abspath(os.getcwd())

try:
    locale.setlocale(locale.LC_ALL, 'russian')
except locale.Error:
    locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')


class Config(object):
    DEBUG = False
    TESTING = False

    LOG = {
        "FILENAME": os.path.join(BASE_DIR, "log", "execom.log"),
        "MAX_BYTES": 1024 * 1024,
        "BACKUP_COUNT": 10,
        "FORMAT": "%(asctime)s[%(levelname)s]:\t%(message)s\tin %(module)s at %(lineno)d",
    }

    VIEW_CASE = "edit_case"

    UPLOAD_PATH = os.path.join(BASE_DIR, "upload")
    # UPLOAD_FOLDER = './static/upload/'
    # ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # configuration page num
    RECORDS_ON_PAGE = 50
    # PER_PAGE = 10

    STATIC_FOLDER = os.path.join(BASE_DIR, 'static')
    TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'templates')


class ProductionConfig(Config):
    pass


class DebugConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    TESTING = True


app_config = {
    'development': DebugConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
}
