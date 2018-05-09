from flask import Blueprint, jsonify, request
from sqlalchemy import func

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


def get_int(argname, default=0):
    try:
        return int(request.args.get(argname))
    except (ValueError, TypeError):
        return default

@world_api.route("/", methods=['GET'])
def world_list():
    """
    Render world list
    """
    count = get_int('count', None)
    shuffle = get_int('random', False)

    img_path = "http://localhost:5000/static/images/world"

    query = World.query
    if shuffle:
        query = query.order_by(func.random())
    worlds = query.paged(count=count)

    return jsonify(
        count=count,
        shuffle=shuffle,
        items=[w.toDict(img_path) for w in worlds.items],
        pages={
            'page': worlds.page,
            'pages': worlds.pages,
            'total': worlds.total,
        },
    )


@world_api.route("/list", methods=['GET'])
def world_random():
    """
    Render random worlds
    """
    try:
        count = int(request.args.get('count'))
    except (ValueError, TypeError):
        count = 1

    try:
        shuffle = int(request.args.get('random'))
    except (ValueError, TypeError):
        shuffle = False

    worlds = list_worlds()
    if shuffle:
        random.shuffle(worlds)

    img_path = "http://localhost:5000/static/images/world"
    return jsonify(
        worlds=[world.as_dict(img_path) for world  in worlds[:count]],
    )
