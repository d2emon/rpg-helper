from flask_script import Manager
from app import db

from generator.space.fixtures import galaxy_names
from world.models import GalaxyName, GalaxyType
# from .models import User, Role
# from .utils import cls, input_username, input_password, input_new_password, show_menu, list_users, show_user


manager = Manager(usage="Admin utils")


def filldata(c, data=[]):
    for title in data:
        g = c(title=title)
        db.session.add(g)
    db.session.commit()
    print("Filled")
    return

# Menu Items
@manager.command
def fillgalaxynames():
    filldata(GalaxyName, galaxy_names[0])
    return


@manager.command
def fillgalaxynames1():
    gn = galaxy_names[1]
    print(gn)
    return


@manager.command
def fillgalaxynames2():
    gn = galaxy_names[2]
    print(gn)
    return


@manager.command
def fillgalaxytypes():
    filldata(GalaxyType, galaxy_names[3])
    return