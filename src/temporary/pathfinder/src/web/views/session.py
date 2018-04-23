#! /usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, redirect, session, flash
from flask.helpers import url_for

from web import app
from web.forms import SessionForm

from models.rpa import GameSession
from db import db_session


@app.route("/session")
def session_list():
    # rpg = current_rpg()
    campaign = session.get("campaign", None)
    if campaign is None:
        return redirect(url_for('campaign_list'))

    sessions = GameSession.query.filter(GameSession.campaign_id == campaign.id).all()
    return render_template("session/list.html", sessions=sessions)


@app.route("/session/add", methods=('GET', 'POST'))
@app.route("/session/edit/<int:session_id>", methods=('GET', 'POST'))
def session_edit(session_id=0):
    if session_id > 0:
        gs = GameSession.query.get(session_id)
    else:
        gs = GameSession()
        gs.campaign_id = session["campaign"].id

    form = SessionForm()
    if form.validate_on_submit():
        gs.title = form.title.data
        gs.real_date = form.real_date.data
        gs.world_date = form.world_date.data
        gs.description = form.description.data

        db_session.add(gs)
        db_session.commit()

        flash("Сессия {} успешно добавлена".format(gs))
        return redirect(url_for('session_list'))

    form.title.data = gs.title
    form.real_date.data = gs.real_date
    form.world_date.data = gs.real_date
    form.description.data = gs.description

    if gs.id:
        session_id = gs.id
    return render_template("session/edit.html", form=form, session_id=session_id)


@app.route("/session/del/<int:session_id>")
def session_del(session_id):
    gs = GameSession.query.get(session_id)
    flash("Сессия {} успешно удалена".format(gs))
    db_session.delete(gs)
    db_session.commit()

    return redirect(url_for("session_list"))


@app.route("/session/<int:session_id>")
def session_show(session_id):
    gs = GameSession.query.get(session_id)
    session["session"] = gs

    return redirect(url_for("char_list"))
    # return render_template("campaigns.html", campaigns=campaigns, selected=games[rpg_id])
