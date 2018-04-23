from flask import Blueprint, render_template
# from flask_login import login_required, login_user, logout_user


tnt = Blueprint('tnt', __name__)


@tnt.route('/')
# @login_required
def index():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Tunels&Trolls")
