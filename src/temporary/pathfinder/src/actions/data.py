#! /usr/bin/env python
# -*- coding:utf-8 -*-
import gen.adventure
import gen.equipment
import gen.encounter
import generate

import actions.editions


CMDS = {
    "adventure": gen.adventure.main,
    "equipment": gen.equipment.main,

    "encounter": gen.encounter.action,
    "generate": generate.action,
}


ACTIONS = [
    {"title": "Book", "action": actions.editions.menu, "id": 21},
    {"title": "Adventure", "action": CMDS["adventure"], "id": 1},
    {"title": "Art Object", "action": CMDS["equipment"], "id": 2},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Adventure"},
    {"title": "Encounter", "action": CMDS["encounter"], "id": 19},
    {"title": "Generator", "action": CMDS["generate"], "id": 20},
]
