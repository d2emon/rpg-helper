from flask import Blueprint, render_template, redirect, url_for, flash, request

from app import app, db

from world.models import World, Galaxy, Star
from .forms import WorldForm, GalaxyForm, StarForm


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
        "app/form.html",
        title=title,
        form=form,
    )


@world.route("/<int:world_id>/del")
def world_del(world_id):
    world = World.query.filter_by(id=world_id).first_or_404()
    db.session.delete(world)
    db.session.commit()
    flash("Мир {} успешно удален".format(world))

    return redirect(url_for("world.world_list", world_id=world_id))


@world.route("/0")
@world.route("/<int:world_id>")
def world_show(world_id=0):
    try:
        page = int(request.args.get('page'))
    except (ValueError, TypeError):
        page = 1

    if world_id:
        world = World.query.filter_by(id=world_id).first_or_404()
    else:
        world = World()

    galaxies = Galaxy.query.filter_by(world_id=world_id).paginate(page, app.config.get('RECORDS_ON_PAGE'))
    
    stars = []
    planets = []


    return render_template(
        "world/view.html",
        title=str(world),
        world_id=world_id,
        world=world,
        galaxies=galaxies.items + [Galaxy.generate() for i in range(10)],
        stars=stars,
        planets=planets,
    )


@world.route("/galaxy/add", methods=('GET', 'POST'))
@world.route("/galaxy/<int:galaxy_id>/edit", methods=('GET', 'POST'))
def galaxy_edit(galaxy_id=0):
    world_id = request.args.get("world_id")
    galaxy_title = request.args.get("galaxy_title")
    if galaxy_id > 0:
        galaxy = Galaxy.query.filter_by(id=galaxy_id).first_or_404()
        title = "Edit Galaxy"
    else:
        galaxy = Galaxy.generate(world_id=world_id, title=galaxy_title)
        title = "New Galaxy"

    form = GalaxyForm(obj=galaxy)
    if form.validate_on_submit():
        form.populate_obj(galaxy)
        db.session.add(galaxy)
        db.session.commit()

        flash("Галактика {} успешно добавлена".format(galaxy))
        return redirect(url_for("world.world_show", world_id=galaxy.world_id))
    return render_template(
        "app/form.html",
        title=title,
        form=form,
    )


@world.route("/galaxy/<int:world_id>/del")
def galaxy_del(world_id):
    galaxy = Galaxy.query.filter_by(id=galaxy_id).first_or_404()
    db.session.delete(galaxy)
    db.session.commit()
    flash("Мир {} успешно удален".format(galaxy))

    return redirect(url_for("world.galaxy_list", galaxy_id=galaxy_id))


@world.route("/galaxy")
@world.route("/galaxy/<int:id>")
def galaxy_show(id=0):
    try:
        page = int(request.args.get('page'))
    except (ValueError, TypeError):
        page = 1

    if id:
        galaxy = Galaxy.query.filter_by(id=id).first_or_404()
    else:
        world_id = request.args.get("world_id")
        galaxy_title = request.args.get("galaxy_title")
        galaxy = Galaxy(world_id=world_id, title=galaxy_title)

    stars = Star.query.filter_by(galaxy_id=id).paginate(page, app.config.get('RECORDS_ON_PAGE'))
    
    planets = []
    print(galaxy)


    return render_template(
        "world/view_galaxy.html",
        title=str(galaxy),
        galaxy_id=id,
        galaxy=galaxy,
        stars=stars.items + [Star(title="Star %d" % (i + 1)) for i in range(10)],
        planets=planets,
    )


@world.route("/star/add", methods=('GET', 'POST'))
@world.route("/star/<int:id>/edit", methods=('GET', 'POST'))
def star_edit(id=0):
    galaxy_id = request.args.get("galaxy_id")
    star_title = request.args.get("title")
    if id > 0:
        star = Star.query.filter_by(id=id).first_or_404()
        title = "Edit Star"
    else:
        star = Star(galaxy_id=galaxy_id, title=star_title)
        title = "New Star"

    form = StarForm(obj=star)
    if form.validate_on_submit():
        form.populate_obj(star)
        db.session.add(star)
        db.session.commit()

        flash("Галактика {} успешно добавлена".format(star))
        return redirect(url_for("world.galaxy_show", id=star.id))
    return render_template(
        "app/form.html",
        title=title,
        form=form,
    )


@world.route("/star/<int:id>/del")
def star_del(id):
    star = Star.query.filter_by(id=id).first_or_404()
    db.session.delete(star)
    db.session.commit()
    flash("Мир {} успешно удален".format(star))

    return redirect(url_for("world.galaxy_show", galaxy_id=star.galaxy_id))
