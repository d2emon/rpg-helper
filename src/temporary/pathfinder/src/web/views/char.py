#! /usr/bin/env python
# -*- coding:utf-8 -*-
from flask import g, render_template, redirect, session
from flask.helpers import url_for
from web import app
from web.models import pc
from models.race import Race


@app.route("/char")
def char_list():
    g.pc = pc
    g.selected = pc[0]
    return redirect(url_for("charsheet", char_id=g.selected.id))


@app.route("/char/add")
def char_add():
    g.pc = pc
    g.selected = pc[0]
    return render_template("char/add.html")


@app.route("/char/del")
def char_del():
    return redirect(url_for("char_list"))


@app.route("/char/<int:char_id>")
def charsheet(char_id):
    print(session["session"])
    if char_id <= 0:
        return redirect(url_for("char_list"))

    g.pc = pc
    g.selected = pc[char_id - 1]
    return render_template("char/view.html")


@app.route("/race/select")
def race_sel():
    # import random
    import pathfinder.character.rooster
    import pathfinder.race
    rooster = pathfinder.character.rooster.Rooster()
    # rooster.load(filename)
    rooster.add(count=5)
    rooster.defineAbility()

    # races = [random.choice(list(pathfinder.race.RACES.keys())) for i in rooster.chars]
    races = Race.query.all()
    return render_template("char/races.html", races=races)


@app.route("/race/<int:race_id>")
def race_show(race_id=None):
    import logging
    logging.debug("Race #%d", race_id)

    race = Race.query.get(race_id)
    return render_template("char/show-race.html", race=race)
