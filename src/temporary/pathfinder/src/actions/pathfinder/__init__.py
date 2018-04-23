#! /usr/bin/env python
# -*- coding:utf-8 -*-
import gui.menu
from actions.pathfinder.generate import generate


PATHFINDER = [
    {"book": "PathC", "title": "1.Getting Started", "action": generate},
    {"book": "PathC", "title": "2.Races"},
    {"book": "PathC", "title": "3.Classes"},
    {"book": "PathC", "title": "4.Skills"},
    {"book": "PathC", "title": "5.Feats"},
    {"book": "PathC", "title": "6.Equipment"},
    {"book": "PathC", "title": "7.Additional"},
    {"book": "PathC", "title": "8.Combat"},
    {"book": "PathC", "title": "9.Magic"},
    {"book": "PathC", "title": "10.Spells"},
    {"book": "PathC", "title": "11.Prestige Classes"},
    {"book": "PathC", "title": "12.Gamemastering"},
    {"book": "PathC", "title": "13.Environment"},
    {"book": "PathC", "title": "14.Creating NPC"},
    {"book": "PathC", "title": "15.Magic Items"},

    {"book": "PathC", "title": "A1.Special Abilities"},
    {"book": "PathC", "title": "A2.Conditions"},

    {"book": "PathA", "title": "1.Races"},
    {"book": "PathA", "title": "2.Classes"},
    {"book": "PathA", "title": "3.Feats"},
    {"book": "PathA", "title": "4.Equipment"},
    {"book": "PathA", "title": "5.Spells"},
    {"book": "PathA", "title": "6.Magic Items"},
    {"book": "PathA", "title": "7.New Rules"},
]


def chapters(id):
    chapter_id = gui.menu.showMenu(items=PATHFINDER)

    from gui import logger
    logger.debug("Chapter #%d", chapter_id)
    chapter = PATHFINDER[chapter_id]
    logger.debug("Chapter %s", chapter)
    action = chapter.get("action")
    if action is not None:
        r = action()
        print(r)
        return True

    r = gui.menu.showMenu(items=["{title} ({book})".format(
        title=u.get("title", "\u2026"),
        book=u.get("book", ""),
    ) for u in PATHFINDER])
    print("r=", r)
    a = r.get("action")
    if a is not None:
        r = a()
        print("a=", r)
    return id
