from flask import Blueprint, render_template, redirect, url_for, flash, request

from app import app, db

from world.models import World

from world.galaxy.models import GalaxyName, GalaxyPlacement, GalaxyForm, GalaxyType
from world.galaxy.forms import GalaxyNameForm, GalaxyPlacementForm, GalaxyFormForm, GalaxyTypeForm
from world.star.models import StarType
from world.star.forms import StarTypeForm


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
    

def list_model(modelclass, **kwargs):
    try:
        page = int(request.args.get('page'))
    except (ValueError, TypeError):
        page = 1
    
    pagination = modelclass.query.paginate(page, app.config.get('RECORDS_ON_PAGE'))
    return render_template(
        'admin/list_galaxy.html',
        title=kwargs.get('title', "Model"),
        items=pagination.items,
        pagination=pagination,
        edit=kwargs.get('edit_link', "admin.model_edit"),
        del_link=kwargs.get('del_link', "admin.model_del"),
    )


def edit_model(modelclass, id, modelformclass, **kwargs):
    title = kwargs.get('title', "Model")
    if id > 0:
        model = modelclass.query.filter_by(id=id).first_or_404()
        title = "Edit %s" % (title)
    else:
        model = modelclass()
        title = "New %s" % (title)

    form = modelformclass(obj=model)
    if form.validate_on_submit():
        form.populate_obj(model)
        db.session.add(model)
        db.session.commit()

        flash("Мир {} успешно добавлен".format(model))
        redirect_link = kwargs.get('redirect_link', "admin.model_list")
        return redirect(url_for(redirect_link))
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

    redirect_link = kwargs.get('redirect_link', "admin.model_list")
    return redirect(url_for(redirect_link))


@admin.route("/galaxy/name")
def galaxy_name_list():
    """
    Render galaxy admin page
    """
    return list_model(
        GalaxyName,
        title="Galaxy Names",
        edit_link='admin.galaxy_name_edit',
        del_link='admin.galaxy_name_del',
    )


@admin.route("/galaxy/name/add", methods=('GET', 'POST'))
@admin.route("/galaxy/name/<int:id>/edit", methods=('GET', 'POST'))
def galaxy_name_edit(id=0):
    return edit_model(
        GalaxyName,
        id,
        GalaxyNameForm,
        title="Galaxy Name",
        redirect_link='admin.galaxy_name_list',
    )


@admin.route("/galaxy/name/<int:id>/del")
def galaxy_name_del(id):
    return del_model(
        GalaxyName,
        id,
        redirect_link='admin.galaxy_name_list',
    )


@admin.route("/galaxy/placement")
def galaxy_placement_list():
    """
    Render galaxy admin page
    """
    return list_model(
        GalaxyPlacement,
        title="Galaxy Placements",
        edit_link='admin.galaxy_placement_edit',
        del_link='admin.galaxy_placement_del',
    )


@admin.route("/galaxy/placement/add", methods=('GET', 'POST'))
@admin.route("/galaxy/placement/<int:id>/edit", methods=('GET', 'POST'))
def galaxy_placement_edit(id=0):
    return edit_model(
        GalaxyPlacement,
        id,
        GalaxyPlacementForm,
        title="Galaxy Placement",
        redirect_link='admin.galaxy_placement_list',
    )


@admin.route("/galaxy/placement/<int:id>/del")
def galaxy_placement_del(id):
    return del_model(
        GalaxyPlacement,
        id,
        redirect_link='admin.galaxy_placement_list',
    )


@admin.route("/galaxy/form")
def galaxy_form_list():
    """
    Render galaxy admin page
    """
    return list_model(
        GalaxyForm,
        title="Galaxy Forms",
        edit_link='admin.galaxy_form_edit',
        del_link='admin.galaxy_form_del',
    )


@admin.route("/galaxy/form/add", methods=('GET', 'POST'))
@admin.route("/galaxy/form/<int:id>/edit", methods=('GET', 'POST'))
def galaxy_form_edit(id=0):
    return edit_model(
        GalaxyForm,
        id,
        GalaxyFormForm,
        title="Galaxy Form",
        redirect_link='admin.galaxy_form_list',
    )


@admin.route("/galaxy/form/<int:id>/del")
def galaxy_form_del(id):
    return del_model(
        GalaxyForm,
        id,
        redirect_link='admin.galaxy_form_list',
    )


@admin.route("/galaxy/type")
def galaxy_type_list():
    """
    Render galaxy admin page
    """
    return list_model(
        GalaxyType,
        title="Galaxy Types",
        edit_link='admin.galaxy_type_edit',
        del_link='admin.galaxy_type_del',
    )


@admin.route("/galaxy/type/add", methods=('GET', 'POST'))
@admin.route("/galaxy/type/<int:id>/edit", methods=('GET', 'POST'))
def galaxy_type_edit(id=0):
    return edit_model(
        GalaxyType,
        id,
        GalaxyTypeForm,
        title="Galaxy Type",
        redirect_link='admin.galaxy_type_list',
    )


@admin.route("/galaxy/type/<int:id>/del")
def galaxy_type_del(id):
    return del_model(
        GalaxyType,
        id,
        redirect_link='admin.galaxy_type_list',
    )


@admin.route("/star/type")
def star_type_list():
    """
    Render star admin page
    """
    return list_model(
        StarType,
        title="Star Types",
        edit_link='admin.star_type_edit',
        del_link='admin.star_type_del',
    )


@admin.route("/star/type/add", methods=('GET', 'POST'))
@admin.route("/star/type/<int:id>/edit", methods=('GET', 'POST'))
def star_type_edit(id=0):
    return edit_model(
        StarType,
        id,
        StarTypeForm,
        title="Galaxy Type",
        redirect_link='admin.star_type_list',
    )


@admin.route("/star/type/<int:id>/del")
def star_type_del(id):
    return del_model(
        StarType,
        id,
        redirect_link='admin.star_type_list',
    )

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