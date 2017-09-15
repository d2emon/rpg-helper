from flask import Blueprint, render_template
# from flask_login import login_required, login_user, logout_user

from .models import games

rpg = Blueprint('rpg', __name__)


@rpg.route('/')
# @login_required
def index():
    """
    Render the homepage template on the / route
    """
    return render_template(
        'rpg/list.html',
        title="Game Systems",
        games=games,
        items=games,
        # items=GamesList(),
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
