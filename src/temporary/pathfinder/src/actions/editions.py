#! /usr/bin/env python
# -*- coding:utf-8 -*-
import logging
import gui.menu

import actions.books
import actions.pathfinder


def dnd(id):
    r = gui.menu.showMenu(items=actions.books.DND3)
    print(r)
    return id


def cyclo(id):
    r = gui.menu.showMenu(items=actions.books.DND1)
    print(r)
    return id


UNITS = [
    {"title": "Pathfinder", "action": actions.pathfinder.chapters},
    {"title": "DnD 3.5", "action": dnd},
    {"title": "Cyclopedia", "action": cyclo},
]


def selectBook(bookId):
    logging.debug("Book #%d - %s", bookId, UNITS[bookId])
    book = UNITS[bookId].get("action", None)
    return book(bookId)


def menu(actionId):
    r = gui.menu.showMenu(items=[u["title"] for u in UNITS], func=selectBook)
    logging.debug("Book: %s", r)
    return r
