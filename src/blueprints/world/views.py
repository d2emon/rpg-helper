from flask import Blueprint, render_template, redirect, url_for, flash, request

from app import app, db

from .models import World
from .forms import WorldForm
from .galaxy.models import Galaxy
from .galaxy.forms import GalaxyForm
from .star.models import Star
from .star.forms import StarForm
from .planet.models import Planet
from .planet.forms import PlanetForm


world = Blueprint('world', __name__)


@world.route("/list")
def world_list():
    """
    Render world list
    """
    worlds = World.query.paged()
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


def edit_model(modelclass, id, modelformclass, **kwargs):
    title = kwargs.get('title', "Model")
    new_model = kwargs.get('new_model', None)
    
    if id > 0:
        model = modelclass.query.filter_by(id=id).first_or_404()
        title = "Edit %s" % (title)
    else:
        if new_model is None:
            model = modelclass()
        else:
            model = new_model
        title = "New %s" % (title)

    form = modelformclass(obj=model)
    if form.validate_on_submit():
        form.populate_obj(model)
        db.session.add(model)
        db.session.commit()

        flash("Мир {} успешно добавлен".format(model))
        redirect_link = kwargs.get('redirect_link', "world.world_show")
        return redirect(url_for(redirect_link, id=model.id))
    return render_template(
        "app/form.html",
        title=title,
        form=form,
    )


def del_model(modelclass, id, **kwargs):
    model = modelclass.query.filter_by(id=id).first_or_404()
    db.session.delete(model)
    db.session.commit()
    flash("Мир {} успешно удален".format(model))
    redirect_link = kwargs.get('redirect_link', "world.world_show")
    return redirect(url_for(redirect_link))


@world.route("/galaxy/add", methods=('GET', 'POST'))
@world.route("/galaxy/<int:id>/edit", methods=('GET', 'POST'))
def galaxy_edit(id=0):
    world_id = request.args.get("world_id")
    galaxy_title = request.args.get("galaxy_title")
    return edit_model(
        Galaxy, 
        id, 
        GalaxyForm,
        title="Galaxy",
        new_model=Galaxy.generate(title=galaxy_title, world_id=world_id),
        redirect_link="world.galaxy_show"
    )


@world.route("/galaxy/<int:id>/del")
def galaxy_del(id):
    return del_model(
        Galaxy,
        id,
        redirect_link="world.galaxy_list"
    )


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
        db.session.add(galaxy)
        db.session.commit()
        return redirect(url_for("world.galaxy_show", id=galaxy.id))

    star_list = Star.query.filter_by(galaxy_id=id).paginate(page, app.config.get('RECORDS_ON_PAGE'))
    stars = star_list.items
    
    planets = []
    
    return render_template(
        "world/view_galaxy.html",
        title=str(galaxy),
        galaxy_id=id,
        galaxy=galaxy,
        stars=stars  + [Star().generate() for i in range(10)],
        planets=planets,
    )


def generate_star(**kwargs):
    galaxy_id = kwargs.get("galaxy_id")
    star_type = kwargs.get("star_type")
    star_title = kwargs.get("title")
    image = kwargs.get("image")
    s = Star.generate(galaxy_id=galaxy_id, title=star_title, image=image, star_type=star_type)
    Planet().generate_planets(s)
    return s


@world.route("/star/add", methods=('GET', 'POST'))
@world.route("/star/<int:id>/edit", methods=('GET', 'POST'))
def star_edit(id=0):
    galaxy_id = request.args.get("galaxy_id")
    star_type = request.args.get("star_type")
    star_title = request.args.get("title")
    image=request.args.get("image")
    return edit_model(
        Star, 
        id, 
        StarForm,
        title="Star",
        # new_model=Star.generate(galaxy_id=galaxy_id, title=star_title, image=image, star_type=star_type),
        new_model=generate_star(galaxy_id=galaxy_id, title=star_title, image=image, star_type=star_type),
        redirect_link="world.galaxy_show"
    )


@world.route("/star/<int:id>/del")
def star_del(id):
    return del_model(
        Star,
        id,
        redirect_link="world.galaxy_show"
    )


@world.route("/star")
@world.route("/star/<int:id>")
def star_show(id=0):
    try:
        page = int(request.args.get('page'))
    except (ValueError, TypeError):
        page = 1

    if id:
        star = Star.query.filter_by(id=id).first_or_404()
    else:
        galaxy_id = request.args.get("galaxy_id")
        star_type = request.args.get("star_type")
        star_title = request.args.get("title")
        image=request.args.get("image")
        # star = Star.generate(galaxy_id=galaxy_id, title=star_title, image=image, star_type=star_type)
        star = generate_star(galaxy_id=galaxy_id, title=star_title, image=image, star_type=star_type)
        db.session.add(star)
        db.session.commit()
        return redirect(url_for("world.star_show", id=star.id))

    # stars = Star.query.filter_by(galaxy_id=id).paginate(page, app.config.get('RECORDS_ON_PAGE'))
    
    planets = Planet.query.filter_by(star_id=id).order_by(Planet.from_sun).all()
    
    return render_template(
        "world/view_star.html",
        title=str(star),
        star_id=id,
        star=star,
        planets=planets,
    )


@world.route("/planet/add", methods=('GET', 'POST'))
@world.route("/planet/<int:id>/edit", methods=('GET', 'POST'))
def planet_edit(id=0):
    star_id = request.args.get("star_id")
    planet_type = request.args.get("planet_type")
    planet_title = request.args.get("title")
    image=request.args.get("image")
    return edit_model(
        Planet, 
        id, 
        PlanetForm,
        title="planet",
        new_model=Planet.generate(star_id=star_id, title=planet_title, image=image, planet_type=planet_type),
        redirect_link="world.planet_show"
    )


@world.route("/planet/<int:id>/del")
def planet_del(id):
    return del_model(
        Planet,
        id,
        redirect_link="world.star_show"
    )


@world.route("/planet")
@world.route("/planet/<int:id>")
def planet_show(id=0):
    try:
        page = int(request.args.get('page'))
    except (ValueError, TypeError):
        page = 1

    if id:
        planet = Planet.query.filter_by(id=id).first_or_404()
    else:
        star_id = request.args.get("star_id")
        planet_type = request.args.get("planet_type")
        planet_title = request.args.get("title")
        image=request.args.get("image")
        planet = Planet.generate(star_id=star_id, title=planet_title, image=image, planet_type=planet_type)
        db.session.add(planet)
        db.session.commit()

    # planets = Planet.query.filter_by(star_id=id).all()
    
    return render_template(
        "world/view_planet.html",
        title=str(planet),
        planet_id=id,
        planet=planet,
        # planets=planets + [Planet().generate() for i in range(10)],
    )