"""
    manager.py
    ~~~~~~~~~~~

    flask manager script

    :copyright: (c) 2013.
    :license: BSD, see LICENSE for more details.
"""
from flask_migrate import MigrateCommand
from flask_script import Manager, Server, prompt_bool
from app import manager, db


# Add commands
manager.add_command("listenserver", Server('0.0.0.0', port=5000))
manager.add_command('db', MigrateCommand)


@manager.command
def createall():
    "Creates database tables"
    db.create_all()


@manager.command
def dropall():
    "Drops all database tables"

    if prompt_bool("Are you sure? You will lose all your data!"):
        db.drop_all()
