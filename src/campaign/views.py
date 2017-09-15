from flask import Blueprint, render_template


campaign = Blueprint('campaign', __name__)


@campaign.route("/list")
def campaign_list():
    """
    Render campaign list
    """
    # # rpg = current_rpg()
    # rpg = session.get("rpg", None)
    # if rpg is None:
    #     return redirect(url_for('rpg_list'))

    # campaigns = Campaign.query.filter(Campaign.gs_id==rpg.id).all()
    # return render_template("campaign/list.html", campaigns=campaigns)
    return render_template('home/index.html', title="Campaigns")


@campaign.route("/add", methods=('GET', 'POST'))
@campaign.route("/edit/<int:campaign_id>", methods=('GET', 'POST'))
def campaign_edit(campaign_id=0):
    """
    Edit campaign
    """
    # if campaign_id > 0:
    #     campaign = Campaign.query.get(campaign_id)
    # else:
    #     campaign = Campaign()
    #     campaign.gs_id = session["rpg"].id

    # form = CampaignForm()
    # if form.validate_on_submit():
    #     campaign.title = form.title.data
    #     db_session.add(campaign)
    #     db_session.commit()

    #     flash("Кампания {} успешно добавлена".format(campaign))
    #     return redirect(url_for('campaign_list'))
    # form.title.data = campaign.title
    # return render_template("campaign/edit.html", form=form, campaign_id=campaign.id)


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


@campaign.route("/<int:campaign_id>")
def campaign_show(campaign_id):
    """
    Show campaign
    """
    # campaign = Campaign.query.get(campaign_id)
    # session["campaign"] = campaign

    # return redirect(url_for("session_list"))
    # # return render_template("campaigns.html", campaigns=campaigns, selected=games[rpg_id])
