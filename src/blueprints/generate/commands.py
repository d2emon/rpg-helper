from flask_script import Manager
from app import db

# from blueprints.world.default import worlds
# from blueprints.world.models import World
from generator.world import WorldGenerator
from generator.album import AlbumGenerator
from generator.band import BandGenerator


manager = Manager(usage="Generators")


def get_int(arg, default=1):
    try:
        return int(arg)
    except (ValueError, TypeError):
        return default


# Menu Items
@manager.command
def world(count=1):
    """
    World generator
    """
    count = get_int(count)

    for i in range(count):
        g = WorldGenerator.generate()
        print(g)
    return


@manager.command
def album(count=1):
    """
    Album generator
    """
    count = get_int(count)

    for i in range(count):
        g = AlbumGenerator.generate()
        print(g)
    return


@manager.command
def band(count=1):
    """
    Band generator
    """
    count = get_int(count)

    for i in range(count):
        g = BandGenerator.generate()
        print(g)
    return
