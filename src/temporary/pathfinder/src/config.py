import os
basedir = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/gurps.db')
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

SECRET_KEY = "some key"
SESSION_TYPE = "filesystem"
SESSION_FILE_DIR = "../flask_session"
