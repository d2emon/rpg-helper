from flask import Blueprint, render_template
# from flask_login import login_required, login_user, logout_user


gurps = Blueprint('gurps', __name__)


@gurps.route('/')
# @login_required
def index():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="GURPS")
