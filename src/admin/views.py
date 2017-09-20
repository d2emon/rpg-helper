from flask import Blueprint, render_template, redirect, url_for, flash, request

from app import app, db

from world.models import World, GalaxyName
from world.forms import WorldForm, GalaxyNameForm


admin = Blueprint('admin', __name__)


@admin.route("/")
def index():
    """
    Render main admin page
    """
    return render_template(
        'admin/index.html',
        title="Admin",
    )


@admin.route("/galaxy")
def galaxy_list():
    """
    Render galaxy admin page
    """
    try:
        page = int(request.args.get('page'))
    except (ValueError, TypeError):
        page = 1
    
    galaxies = GalaxyName.query.paginate(page, app.config.get('RECORDS_ON_PAGE'))
    return render_template(
        'admin/list_galaxy.html',
        title="Galaxy",
        items=galaxies.items,
        pagination=galaxies,
    )


@admin.route("/galaxy/add", methods=('GET', 'POST'))
@admin.route("/galaxy/<int:galaxy_id>/edit", methods=('GET', 'POST'))
def galaxy_edit(galaxy_id=0):
    if galaxy_id > 0:
        gn = GalaxyName.query.filter_by(id=galaxy_id).first_or_404()
        title = "Edit Galaxy"
    else:
        gn = GalaxyName()
        title = "New Galaxy"

    form = GalaxyNameForm(obj=gn)
    if form.validate_on_submit():
        form.populate_obj(gn)
        db.session.add(gn)
        db.session.commit()

        flash("Мир {} успешно добавлен".format(gn))
        return redirect(url_for("admin.galaxy_list"))
    return render_template(
        "app/form.html",
        title=title,
        form=form,
    )


@admin.route("/<int:world_id>/del")
def admin_del(world_id):
    world = World.query.filter_by(id=world_id).first_or_404()
    db.session.delete(world)
    db.session.commit()
    flash("Мир {} успешно удален".format(world))

    return redirect(url_for("world.world_list", world_id=world_id))


@admin.route("/<int:world_id>")
def admin_show(world_id):
    world = World.query.filter_by(id=world_id).first_or_404()
    galaxies = []
    stars = []
    planets = []

    random_galaxies = []

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