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


@world_api.route("/names", methods=['GET'])
def names():
    """
    Render names list
    """
    img_path = "{}static/images/world".format(request.url_root)

    sex = get_int('sex')
    models, items, pagination = list_models(World.query)
    # generated.push(names.generate(sex))
    models['names'] = [w.toDict(img_path) for w in items]
    return jsonify(models)


@world_api.route("/clothing", methods=['GET'])
def clothing():
    """
    Render characters clothing
    """
    img_path = "{}static/images/world".format(request.url_root)

    sex = get_int('sex')
    models, items, pagination = list_models(World.query)
    # generated.push(clothing.generate(sex))
    models['sex'] = sex
    models['clothing'] = [w.toDict(img_path) for w in items]
    return jsonify(models)


@world_api.route("/characters", methods=['GET'])
def characters():
    """
    Render characters list
    """
    img_path = "{}static/images/world".format(request.url_root)

    sex = get_int('sex', None)
    models, items, pagination = list_models(World.query)
    # generated.push(aliens.generate())
    models['characters'] = [w.toDict(img_path) for w in items]
    for m in models.get('characters', []):
        if sex is None:
            charSex = random.randrange(2)
        else:
            charSex = sex
        m['count'] = models.get('count')
        m['sex'] = charSex
        m['name'] = "names.generate(charSex)"
        m['clothing'] = "clothing.generate(charSex)"
    return jsonify(models)
