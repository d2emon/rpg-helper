from flask import Blueprint, render_template, url_for
# from flask_login import login_required, login_user, logout_user

from .models import GameSystem

rpg = Blueprint('rpg', __name__)


@rpg.route('/')
# @login_required
def index():
    """
    Render the homepage template on the / route
    """
    games = [
        GameSystem(title="Pathfinder", url=url_for('pathfinder.index')),
        GameSystem(title="GURPS", url=url_for('gurps.index')),
        GameSystem(title="Tunels & Trolls", url=url_for('tnt.index')),
        GameSystem(title="Game", website="http://127.0.0.1:5000/"),
        GameSystem(title="Game1", website="http://127.0.0.1:8000/"),
    ]
    return render_template(
        'rpg/list.html',
        title="Game Systems",
        items=games,
    )
    # return render_template("rpg.html", games=GameSystem.query.all(), selected=current_rpg())


@rpg.route("/add")
def rpg_add():
    return render_template('home/index.html', title="Welcome")
    # return redirect(url_for("campaign_list"))


@rpg.route("/del")
def rpg_del():
    return render_template('home/index.html', title="Welcome")
    # return redirect(url_for("campaign_list"))
