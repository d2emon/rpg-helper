from flask import Blueprint, render_template, redirect, url_for, flash, request

from app import app, db

from world.models import World
from world.forms import WorldForm


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
    return render_template(
        'admin/index.html',
        title="Galaxy",
    )


@admin.route("/add", methods=('GET', 'POST'))
@admin.route("/<int:world_id>/edit", methods=('GET', 'POST'))
def admin_edit(world_id=0):
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