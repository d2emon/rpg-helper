from flask import Blueprint, render_template, redirect, url_for, flash, request

from app import app, db
from .models import Campaign
from .forms import CampaignForm


campaign = Blueprint('campaign', __name__)


@campaign.route("/list")
def campaign_list():
    """
    Render campaign list
    """
    try:
        page = int(request.args.get('page'))
    except (ValueError, TypeError):
        page = 1

    # # rpg = current_rpg()
    # rpg = session.get("rpg", None)
    # if rpg is None:
    #     return redirect(url_for('rpg_list'))

    # campaigns = Campaign.query.filter(Campaign.gs_id==rpg.id).all()
    campaigns = Campaign.query.paginate(page, app.config.get('RECORDS_ON_PAGE'))
    return render_template(
        'campaign/list.html',
        title="Campaigns",
        items=campaigns.items,
        pagination=campaigns,
    )


@campaign.route("/add", methods=('GET', 'POST'))
@campaign.route("/edit/<int:campaign_id>", methods=('GET', 'POST'))
def campaign_edit(campaign_id=0):
    """
    Edit campaign
    """
    if campaign_id:
        campaign = Campaign.query.get(campaign_id)
        title = "Edit Campaign"
    else:
        campaign = Campaign()
        title = "Add Campaign"
    #     campaign.gs_id = session["rpg"].id

    form = CampaignForm(obj=campaign)
    if form.validate_on_submit():
        form.populate_obj(campaign)
        db.session.add(campaign)
        db.session.commit()

        flash("Кампания {} успешно добавлена".format(campaign))
        return redirect(url_for('campaign.campaign_list'))
    return render_template(
        "campaign/edit.html",
        form=form,
        campaign_id=campaign.id,
        title=title,
    )


@campaign.route("/del/<int:campaign_id>")
def campaign_del(campaign_id):
    """
    Delete campaign
    """
    # campaign = Campaign.query.get(campaign_id)
    # flash("Кампания {} успешно удалена".format(campaign))
    # db_session.delete(campaign)
    # db_session.commit()

    # return redirect(url_for("campaign_list"))