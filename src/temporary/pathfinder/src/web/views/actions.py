#! /usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, redirect
from flask.helpers import url_for
from web import app

WEB_CMDS = [
    None,
    'action_adventure',
    'action_equipment',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    'action_encounter',
    'action_generate',
]


ADVENTURE_TYPES = [
    "local",
    "tavern",
    "global",
]


@app.route("/actions")
@app.route("/actions/<int:option_id>")
def action_list(option_id=None):
    from actions.run import ACTIONS
    
    if option_id is not None:
        action = ACTIONS[option_id]
        cmd = WEB_CMDS[action['id']]
        
        import logging
        logging.debug(action)
        logging.debug(cmd)
        return redirect(url_for(cmd))
    action_list = [{"title": a["title"], "url": url_for('action_list', action_id=id), "action": a, } for id, a in enumerate(ACTIONS)]
    return render_template("actions_list.html", title="Выберите действие:", actions=action_list)


@app.route("/adventure")
def action_adventure(option_id=None):
    import logging
    logging.debug("Adventure generation")

    from adventure import FILENAMES
    from adventure import STYLES
    from adventure import Adventure
    default = FILENAMES["local"]
 
    title = "Выберите вид приключения:"
    adventures = STYLES
    # adventures = [Adventure(id=gui.menu.showMenu(title="Select adventure type:", items=STYLES))]
    action_list = [{"title": a.get("title", id), "url": url_for('adventure_show', option_id=ADVENTURE_TYPES[id]), "action": a, } for id, a in enumerate(adventures)]

    logging.debug(adventures)
    for q in adventures:
        logging.debug("-"*80)
        logging.debug(q)
        logging.debug("-"*80)
        # print(q.title)
        # print(q.description)


    return render_template("actions_list.html", title=title, actions=action_list)


@app.route("/adventure/<string:option_id>")
def adventure_show(option_id):
    import logging
    logging.debug("Adventure generation")

    from adventure import FILENAMES
    from adventure import STYLES
    from adventure import Adventure
    default = STYLES[0]
    local_styles = {
        "local": STYLES[0],
        "tavern": STYLES[1],
        "global": STYLES[2],
    }
    logging.debug(option_id)

    adventure = Adventure(style=local_styles.get(option_id, default))
    title = adventure.title

    logging.debug("-"*80)
    logging.debug(adventure)
    logging.debug("-"*80)
    # print(q.title)
    # print(q.description)


    return render_template("adventure.html", adventure=adventure)
