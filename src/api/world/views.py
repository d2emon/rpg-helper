from flask import Blueprint, jsonify, request
from sqlalchemy import func

from app import app # , db

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

    img_path = "{}static/images/world".format(request.url_root)

    query = World.query
    if shuffle:
        query = query.order_by(func.random())
    worlds = query.paged(count=count)

    return jsonify(
        shuffle=shuffle,
        worlds=[w.toDict(img_path) for w in worlds.items],
        page=worlds.page,
        pages=worlds.pages,
        count=count,
        total=worlds.total,
    )


@world_api.route("/list", methods=['GET'])
def world_random():
    """
    Render random worlds
    """
    count = get_int('count', None)
    shuffle = get_int('random', False)

    img_path = "{}/world".format(app.config.get('IMG_URL'))

    worlds = list_worlds()
    if shuffle:
        random.shuffle(worlds)

    return jsonify(
        worlds=[world.as_dict(img_path) for world  in worlds[:count]],
    )
