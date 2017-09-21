from flask import Blueprint, render_template, redirect, url_for, flash, request
from datetime import datetime

from app import app, db

from campaign.views import campaign
from campaign.models import Campaign

from .models import GameSession
from .forms import GameSessionForm


gamesession = Blueprint('session', __name__)


@campaign.route("/campaign-<int:campaign_id>/list")
def session_list(campaign_id):
    """
    Render session list
    """
    # campaigns = Campaign.query.filter(Campaign.gs_id==rpg.id).all()
    campaign = Campaign.query.filter_by(id=campaign_id).first_or_404()
    # sessions = GameSession.query.filter_by(campaign_id=campaign_id).order_by(GameSession.real_date.desc()).paginate(page, app.config.get('RECORDS_ON_PAGE'))
    sessions = GameSession.query.filter_by(campaign_id=campaign_id).order_by(GameSession.real_date.desc()).paged()
    return render_template(
        'session/list.html',
        title="Sessions",
        campaign=campaign,
        campaign_id=campaign_id,
        items=sessions.items,
        pagination=sessions,
    )


@gamesession.route("/campaign-<int:campaign_id>/add", methods=('GET', 'POST'))
@gamesession.route("/campaign-<int:campaign_id>/<int:session_id>/edit", methods=('GET', 'POST'))
def session_edit(campaign_id, session_id=0):
    if session_id > 0:
        gs = GameSession.query.filter_by(id=session_id).first_or_404()
        title = "Edit Session"
    else:
        gs = GameSession(campaign_id=campaign_id, real_date=datetime.today())
        title = "New Session"

    form = GameSessionForm(obj=gs)
    if form.validate_on_submit():
        form.populate_obj(gs)
        # gs.world_date = form.world_date.data
        db.session.add(gs)
        db.session.commit()

        flash("Сессия {} успешно добавлена".format(gs))
        return redirect(url_for("session.session_show", campaign_id=campaign_id, session_id=gs.id))
    return render_template(
        "app/form.html",
        title=title,
        form=form,
    )


@gamesession.route("/campaign-<int:campaign_id>/<int:session_id>/del")
def session_del(campaign_id, session_id):
    gs = GameSession.query.filter_by(id=session_id, campaign_id=campaign_id).first_or_404()
    db.session.delete(gs)
    db.session.commit()
    flash("Сессия {} успешно удалена".format(gs))

    return redirect(url_for("campaign.session_list", campaign_id=campaign_id, session_id=session_id))


@gamesession.route("/campaign-<int:campaign_id>/<int:session_id>")
def session_show(campaign_id, session_id):
    gs = GameSession.query.filter_by(id=session_id, campaign_id=campaign_id).first_or_404()
    # session["session"] = gs

    # return redirect(url_for("session_list", campaign_id=campaign_id, session_id=session_id))
    # return redirect(url_for("char_list"))
    return render_template(
        "session/view.html",
        title=str(gs),
        campaign_id=campaign_id,
        session=gs,
    )