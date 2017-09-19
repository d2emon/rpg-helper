from flask import Blueprint, render_template, redirect, url_for, flash, request

from app import app, db

from .models import World, Galaxy
from .forms import WorldForm, GalaxyForm


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

    random_galaxies = [Galaxy() for i in range(5)]
    for g in random_galaxies:
        g.generate()
    # print(random_galaxies)

    return render_template(
        "world/view.html",
        title=str(world),
        world_id=world_id,
        world=world,
        galaxies=galaxies,
        stars=stars,
        planets=planets,

        random_galaxies=random_galaxies,
    )


@world.route("/galaxy/add", methods=('GET', 'POST'))
@world.route("/galaxy/<int:galaxy_id>/edit", methods=('GET', 'POST'))
def galaxy_edit(galaxy_id=0):
    if galaxy_id > 0:
        galaxy = Galaxy.query.filter_by(id=galaxy_id).first_or_404()
        title = "Edit Galaxy"
    else:
        galaxy = Galaxy()
        galaxy.generate()
        title = "New Galaxy"

    form = GalaxyForm(obj=galaxy)
    if form.validate_on_submit():
        form.populate_obj(galaxy)
        db.session.add(galaxy)
        db.session.commit()

        flash("Галактика {} успешно добавлена".format(galaxy))
        return redirect(url_for("world.world_show", world_id=galaxy.id))
    return render_template(
        "world/edit.html",
        title=title,
        form=form,
        world_id=galaxy_id,
    )
