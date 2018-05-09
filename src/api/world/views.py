from flask import Blueprint, jsonify, request

# from app import app, db

from world.models import World
# from .galaxy.models import Galaxy
# from .galaxy.forms import GalaxyForm
# from .star.models import Star
# from .star.forms import StarForm
# from .planet.models import Planet
# from .planet.forms import PlanetForm
from .models.worlds import World as World1, list_worlds

import random


world_api = Blueprint('world-api', __name__)

images = [
    # "/static/images/world/0-house.jpg",
    # "/static/images/world/0-road.jpg",
    # "/static/images/world/0-plane.jpg",
    # "/static/images/world/0-sunshine.jpg",
    "https://lorempixel.com/400/300/",
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

    worlds = list_worlds()
    if shuffle:
        random.shuffle(worlds)

    img_path = "http://localhost:5000/static/images/world"
    return jsonify(
        worlds=[world.as_dict(img_path) for world  in worlds[:count]],
    )
