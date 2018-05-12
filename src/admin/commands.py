from flask_script import Manager
from app import db

from blueprints.world.default import worlds
from generator.space.fixtures import galaxy_names, suns, atmospheres, allPlanets, environments, maps
from blueprints.world.models import World
from blueprints.world.galaxy.models import GalaxyName, GalaxyPlacement, GalaxyForm, GalaxyType
from blueprints.world.star.models import StarType
from blueprints.world.planet.models import PlanetType, Atmosphere, Environment, SurfaceMap

from npc.default import titles, names
from npc.models import Title, Name


manager = Manager(usage="Admin utils")


def filldata(c, data=[]):
    for fixture in data:
        if fixture is None:
            continue
        g = c.load_fixture(fixture)
        db.session.add(g)
    db.session.commit()
    print("Filled")
    return

# Menu Items
@manager.command
def fillworlds():
    filldata(World, worlds)
    return


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


@manager.command
def fillatmospheres():
    filldata(Atmosphere, atmospheres)
    return


@manager.command
def fillplanets():
    filldata(PlanetType, allPlanets)
    return


@manager.command
def fillenvironments():
    filldata(Environment, environments)
    return


@manager.command
def fillsurfacemaps():
    filldata(SurfaceMap, maps)
    return


@manager.command
def fillpcnames():
    filldata(Title, titles)
    filldata(Name, names)
    print("Filled")
    return
