#! /usr/bin/env python
# -*- coding:utf-8 -*-
from web import app, db
from flask import flash, render_template, redirect, url_for


@app.route("/char")
def character():
    from web.models import GameCharacter
    chars = GameCharacter.query.all()

    return render_template("char_list.html", chars=chars)


@app.route("/char/new", methods=['GET', 'POST'])
def new_character():
    from web.models import GameCharacter
    from web.forms import CharEditForm
    c = GameCharacter()

    c.calcAttributes()
    form = CharEditForm()

    if form.validate_on_submit():
        form.save_char(c)
        db.session.add(c)
        db.session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('character'))
    else:
        form.load_char(c)
    return render_template("char_edit.html", c=c, form=form)


@app.route("/char/id-<int:char_id>", methods=['GET', 'POST'])
def edit_character(char_id):
    from web.models import GameCharacter
    from web.forms import CharEditForm
    c = GameCharacter.query.get(char_id)
    if c is None:
        return redirect(url_for('character'))

    c.calcAttributes()
    form = CharEditForm()

    if form.validate_on_submit():
        form.save_char(c)
        db.session.add(c)
        db.session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('character'))
    else:
        form.load_char(c)
    return render_template("char_edit.html", c=c, form=form)
