from flask import Blueprint, render_template, redirect, url_for, flash, request

from app import app, db

from .models import World
from .forms import WorldForm


world = Blueprint('world', __name__)


@world.route("/list")
def world_list():
    """
    Render world list
    """
    try:
        page = int(request.args.get('page'))
    except (ValueError, TypeError):
        page = 1

    # # rpg = current_rpg()
    # campaign = session.get("campaign", None)
    # if campaign is None:
    #     return redirect(url_for('campaign_list'))

    # campaigns = Campaign.query.filter(Campaign.gs_id==rpg.id).all()
    worlds = World.query.paginate(page, app.config.get('RECORDS_ON_PAGE'))
    return render_template(
        'world/list.html',
        title="Worlds",
        # campaign=campaign,
        # campaign_id=campaign_id,
        items=worlds.items,
        pagination=worlds,
    )


@world.route("/add", methods=('GET', 'POST'))
@world.route("/<int:world_id>/edit", methods=('GET', 'POST'))
def world_edit(world_id=0):
    if world_id > 0:
        world = World.query.filter_by(id=world_id).first_or_404()
        title = "Edit World"
    else:
        world = World()
        title = "New World"

    form = WorldForm(obj=world)
    if form.validate_on_submit():
        form.populate_obj(world)
        db.session.add(world)
        db.session.commit()

        flash("Мир {} успешно добавлен".format(world))
        return redirect(url_for("world.world_show", world_id=world.id))
    return render_template(
        "world/edit.html",
        title=title,
        form=form,
        world_id=world_id,
    )


@world.route("/<int:world_id>/del")
def world_del(world_id):
    world = World.query.filter_by(id=world_id).first_or_404()
    db.session.delete(world)
    db.session.commit()
    flash("Мир {} успешно удален".format(world))

    return redirect(url_for("world.world_list", world_id=world_id))


@world.route("/<int:world_id>")
def world_show(world_id):
    world = World.query.filter_by(id=world_id).first_or_404()
    galaxies = []
    stars = []
    planets = []

    return render_template(
        "world/view.html",
        title=str(world),
        world_id=world_id,
        world=world,
        galaxies=galaxies,
        stars=stars,
        planets=planets,
    )
