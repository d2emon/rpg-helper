from flask_script import Manager
from app import db

from generator.space.fixtures import galaxy_names
from world.models import GalaxyName, GalaxyPlacement, GalaxyForm, GalaxyType


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
def fillgalaxyplacements():
    filldata(GalaxyPlacement, galaxy_names[1])
    return


@manager.command
def fillgalaxyforms():
    filldata(GalaxyForm, galaxy_names[2])
    return


@manager.command
def fillgalaxytypes():
    filldata(GalaxyType, galaxy_names[3])
    return