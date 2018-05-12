from flask import Blueprint, jsonify, request
from sqlalchemy import func

from app import app # , db

from world.models import World
from npc.models import GameCharacter


npc_api = Blueprint('npc-api', __name__)


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


@npc_api.route("/", methods=['GET'])
def names():
    """
    Render names list
    """
    sex = get_int('sex')
    models, items, p = list_models(GameCharacter.query.filter(
        GameCharacter.gender_id == sex
    ))
    models['names'] = [i.toDict() for i in items]
    return jsonify(models)


@npc_api.route("/clothing", methods=['GET'])
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


@npc_api.route("/random", methods=['GET'])
def characters():
    """
    Render characters list
    """
    count = get_int('count', None)
    sex = get_int('sex', None)
    # models, items, pagination = list_models(World.query)
    # generated.push(aliens.generate())
    characters = []
    for i in range(count):
        npc = GameCharacter.generate(sex=sex)
        model = npc.toDict()
        model['clothing'] = "clothing.generate({})".format(sex)
        characters.append(model)
    models = {
        'characters': characters,
        'count': count,
    }
    return jsonify(models)
