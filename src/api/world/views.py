from flask import Blueprint, jsonify, request
from sqlalchemy import func

from app import app # , db

from world.models import World
# from npc.models import GameCharacter

import random


world_api = Blueprint('world-api', __name__)


def get_int(argname, default=0):
    try:
        return int(request.args.get(argname))
    except (ValueError, TypeError):
        return default


def list_models(query):
    count = get_int('count', None)
    shuffle = get_int('random', False)

    if shuffle:
        query = query.order_by(func.random())

    pagination = query.paged(count=count)
    return {
        'count': count,
        'shuffle': shuffle,
        'page': pagination.page,
        'pages': pagination.pages,
        'total': pagination.total,
    }, pagination.items, pagination


@world_api.route("/", methods=['GET'])
def world_list():
    """
    Render world list
    """
    img_path = "{}static/images/world".format(request.url_root)

    models, items, pagination = list_models(World.query)
    models['worlds'] = [w.toDict(img_path) for w in items]
    return jsonify(models)


@world_api.route("/aliens", methods=['GET'])
def aliens():
    """
    Render alien races
    """
    img_path = "{}static/images/world".format(request.url_root)

    models, items, pagination = list_models(World.query)
    # generated.push(aliens.generate())
    models['aliens'] = [w.toDict(img_path) for w in items]
    return jsonify(models)
