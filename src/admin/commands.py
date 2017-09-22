from flask_script import Manager
from app import db

from generator.space.fixtures import galaxy_names
from temporary.generator.fixtures import suns
from world.galaxy.models import GalaxyName, GalaxyPlacement, GalaxyForm, GalaxyType
from world.star.models import StarType


manager = Manager(usage="Admin utils")


def filldata(c, data=[]):
    for fixture in data:
        g = c.load_fixture(fixture)
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


@manager.command
def fillstartypes():
    filldata(StarType, suns)
    return