#! /usr/bin/env python
# -*- coding:utf-8 -*-
from web import app, db
from flask import flash, render_template, redirect, url_for


@app.route("/fraction")
def fraction():
    from web.models import Fraction
    fractions = Fraction.query.all()

    return render_template("fraction_list.html", fractions=fractions)


@app.route("/fraction/new", methods=['GET', 'POST'])
def new_fraction():
    from web.models import Fraction
    from web.forms import FractionEditForm
    f = Fraction()

    form = FractionEditForm()

    if form.validate_on_submit():
        form.save_fraction(f)
        db.session.add(f)
        db.session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('fraction'))
    else:
        form.load_fraction(f)
    return render_template("fraction_edit.html", c=f, form=form)


@app.route("/fraction/id-<int:fraction_id>", methods=['GET', 'POST'])
def edit_fraction(fraction_id):
    from web.models import Fraction
    from web.forms import FractionEditForm
    f = Fraction.query.get(fraction_id)
    if f is None:
        return redirect(url_for('fraction'))

    form = FractionEditForm()

    if form.validate_on_submit():
        form.save_fraction(f)
        db.session.add(f)
        db.session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('fraction'))
    else:
        form.load_fraction(f)
    return render_template("fraction_edit.html", c=f, form=form)


@app.route("/fraction/random")
def random_fraction():
    from web.models import Fraction
    from web.forms import FractionEditForm
    from sqlalchemy.sql.expression import func
    import random

    fraction_count = Fraction.query.filter(Fraction.weight >= 10).count()
    fraction_id = random.randint(0, fraction_count)
    print(fraction_count, fraction_id)
    if fraction_id == 0:
        fractions = [Fraction.query.filter(Fraction.weight < 10).order_by(func.random()).first()]
    else:
        fractions = [Fraction.query.get(fraction_id)]

    return redirect(url_for('edit_fraction', fraction_id=fraction_id))
    return render_template("fraction_list.html", fractions=fractions)

    f = fractions[0]
    if f is None:
        return redirect(url_for('fraction'))

    form = FractionEditForm()

    if form.validate_on_submit():
        form.save_fraction(f)
        db.session.add(f)
        db.session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('fraction'))
    else:
        form.load_fraction(f)
    return render_template("fraction_edit.html", c=f, form=form)
