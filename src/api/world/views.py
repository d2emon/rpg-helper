from flask import Blueprint, jsonify, request

# from app import app, db

from world.models import World
# from .galaxy.models import Galaxy
# from .galaxy.forms import GalaxyForm
# from .star.models import Star
# from .star.forms import StarForm
# from .planet.models import Planet
# from .planet.forms import PlanetForm
from .models.worlds import worlds

import random


world_api = Blueprint('world-api', __name__)

images = [
    'house.jpg',
    'road.jpg',
    'plane.jpg',
    'sunshine.jpg'
]


@world_api.route("/", methods=['GET'])
def world_list():
    """
    Render world list
    """
    worlds = World.query.paged()
    return jsonify(
        # campaign=campaign,
        # campaign_id=campaign_id,
        items=worlds.items,
        # pagination=worlds,
    )


@world_api.route("/list", methods=['GET'])
def world_random():
    """
    Render random worlds
    """
    try:
        count = int(request.args.get('count'))
    except ValueError:
        count = 1

    try:
        shuffle = int(request.args.get('random'))
    except:
        shuffle = False

    if shuffle:
        random.shuffle(worlds)

    return jsonify(
        worlds=[{
            'id': id,
            'title': world,
            'subtitle': "1,000 miles of wonder",
            'src': "/static/images/{}".format(random.choice(images)),
        } for id, world in enumerate(worlds[:count])],
    )
