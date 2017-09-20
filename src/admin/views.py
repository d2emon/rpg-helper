from flask import Blueprint, render_template, redirect, url_for, flash, request

from app import app, db

from world.models import World, GalaxyName, GalaxyType
from world.forms import GalaxyNameForm, GalaxyTypeForm


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


@admin.route("/galaxy/name")
def galaxy_name_list():
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
        title="Galaxy Name",
        items=galaxies.items,
        pagination=galaxies,
        edit='admin.galaxy_name_edit',
        del_link='admin.galaxy_name_del',
    )


@admin.route("/galaxy/name/add", methods=('GET', 'POST'))
@admin.route("/galaxy/name/<int:id>/edit", methods=('GET', 'POST'))
def galaxy_name_edit(id=0):
    if id > 0:
        gn = GalaxyName.query.filter_by(id=id).first_or_404()
        title = "Edit Galaxy Name"
    else:
        gn = GalaxyName()
        title = "New Galaxy Name"

    form = GalaxyNameForm(obj=gn)
    if form.validate_on_submit():
        form.populate_obj(gn)
        db.session.add(gn)
        db.session.commit()

        flash("Мир {} успешно добавлен".format(gn))
        return redirect(url_for("admin.galaxy_name_list"))
    return render_template(
        "app/form.html",
        title=title,
        form=form,
    )


@admin.route("/galaxy/name/<int:id>/del")
def galaxy_name_del(id):
    gn = GalaxyName.query.filter_by(id=id).first_or_404()
    db.session.delete(gn)
    db.session.commit()
    flash("Мир {} успешно удален".format(gn))

    return redirect(url_for("admin.galaxy_name_list"))


@admin.route("/galaxy/type")
def galaxy_type_list():
    """
    Render galaxy admin page
    """
    try:
        page = int(request.args.get('page'))
    except (ValueError, TypeError):
        page = 1
    
    galaxies = GalaxyType.query.paginate(page, app.config.get('RECORDS_ON_PAGE'))
    return render_template(
        'admin/list_galaxy.html',
        title="Galaxy Type",
        items=galaxies.items,
        pagination=galaxies,
        edit='admin.galaxy_type_edit',
        del_link='admin.galaxy_type_del',
    )


@admin.route("/galaxy/type/add", methods=('GET', 'POST'))
@admin.route("/galaxy/type/<int:id>/edit", methods=('GET', 'POST'))
def galaxy_type_edit(id=0):
    if id > 0:
        gn = GalaxyType.query.filter_by(id=id).first_or_404()
        title = "Edit Galaxy Name"
    else:
        gn = GalaxyType()
        title = "New Galaxy Name"

    form = GalaxyTypeForm(obj=gn)
    if form.validate_on_submit():
        form.populate_obj(gn)
        db.session.add(gn)
        db.session.commit()

        flash("Мир {} успешно добавлен".format(gn))
        return redirect(url_for("admin.galaxy_type_list"))
    return render_template(
        "app/form.html",
        title=title,
        form=form,
    )


@admin.route("/galaxy/type/<int:id>/del")
def galaxy_type_del(id):
    gn = GalaxyType.query.filter_by(id=id).first_or_404()
    db.session.delete(gn)
    db.session.commit()
    flash("Мир {} успешно удален".format(gn))

    return redirect(url_for("admin.galaxy_name_list"))


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