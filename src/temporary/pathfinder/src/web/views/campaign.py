#! /usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, redirect, session, flash
from flask.helpers import url_for

from web import app
from web.models import current_rpg

from models.rpa import Campaign
from db import db_session

from web.forms import CampaignForm

@app.route("/campaign")
def campaign_list():
    # rpg = current_rpg()
    rpg = session.get("rpg", None)
    if rpg is None:
        return redirect(url_for('rpg_list'))

    campaigns = Campaign.query.filter(Campaign.gs_id==rpg.id).all() 
    return render_template("campaign/list.html", campaigns=campaigns)


@app.route("/campaign/add", methods=('GET', 'POST'))
@app.route("/campaign/edit/<int:campaign_id>", methods=('GET', 'POST'))
def campaign_edit(campaign_id=0):
    if campaign_id > 0:
        campaign = Campaign.query.get(campaign_id)
    else:
        campaign = Campaign()
        campaign.gs_id = session["rpg"].id

    form = CampaignForm()
    if form.validate_on_submit():
        campaign.title = form.title.data
        db_session.add(campaign)
        db_session.commit()
        
        flash("Кампания {} успешно добавлена".format(campaign))
        return redirect(url_for('campaign_list'))
    form.title.data = campaign.title
    return render_template("campaign/edit.html", form=form, campaign_id=campaign.id)


@app.route("/campaign/del/<int:campaign_id>")
def campaign_del(campaign_id):
    campaign = Campaign.query.get(campaign_id) 
    flash("Кампания {} успешно удалена".format(campaign))
    db_session.delete(campaign)
    db_session.commit()
        
    return redirect(url_for("campaign_list"))


@app.route("/campaign/<int:campaign_id>")
def campaign_show(campaign_id):
    campaign = Campaign.query.get(campaign_id) 
    session["campaign"] = campaign
    
    return redirect(url_for("session_list"))
    # return render_template("campaigns.html", campaigns=campaigns, selected=games[rpg_id])