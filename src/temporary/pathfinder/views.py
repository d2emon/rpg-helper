from flask import Blueprint, redirect, url_for
# from flask import render_template, redirect, session, flash
# from flask_login import login_required, login_user, logout_user

# from app import app, db
# from .models import current_rpg
# from .models.rpa import Campaign
# from .forms import CampaignForm


pathfinder = Blueprint('pathfinder', __name__)


@pathfinder.route('/')
# @login_required
def index():
    """
    Render the homepage template on the / route
    """
    # session["rpg_id"] = rpg_id
    # if rpg_id <= 0:
    #     return redirect(url_for("rpg_list"))

    # session["rpg"] = current_rpg()
    return redirect(url_for("campaign.campaign_list"))
