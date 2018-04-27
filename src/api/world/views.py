from flask import Blueprint, jsonify

# from app import app, db

from world.models import World
# from .galaxy.models import Galaxy
# from .galaxy.forms import GalaxyForm
# from .star.models import Star
# from .star.forms import StarForm
# from .planet.models import Planet
# from .planet.forms import PlanetForm


world_api = Blueprint('world-api', __name__)


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
