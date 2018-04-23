#! /usr/bin/env python
# -*- coding:utf-8 -*-


import logging
import random

import gui
import gui.commandline
import pathfinder.ruleset
import pathfinder.race


import pathfinder.charsheet
import pathfinder.character.rooster
import pathfinder.charclass


def pickClass(chars=[], classes=[]):
    # TODO: Pick Class
    logging.info("Pick Your Class")
    return []


def pickSkills(chars=[]):
    # TODO: Pick Skills
    print("Pick Skills and Select Feats")
    return []


def buyEquipment(chars=[]):
    # TODO: Buy Equipment
    print("Buy Equipment")
    return []


def finishDetails(chars=[]):
    # TODO: Finish details
    print("Finishing Details")
    return []


def createChars(rooster=pathfinder.character.rooster.Rooster()):
    logging.debug("generate.createChars():Rooster %s", rooster)
    for c in rooster.chars:
        print("-" * 80)
        pathfinder.charsheet.showChar(c)
    print("-" * 80)
    for i in range(1, 11):
        l = pathfinder.charclass.Level(i)
        print("%d\t%d\t%s\t%s\t%s" % (i, l.toNext(), l.ability, l.skill, l.feat))
    l = pathfinder.charclass.xpToLevel(10000)
    print("%d\t%d\t%s\t%s\t%s" % (i, l.toNext(), l.ability, l.skill, l.feat))

    return rooster


def action(action_id):
    return main()


def main(**options):  # pragma: no cover
    logging.info("Starting generator")

    pathfinder.ruleset.rules.rollMethod = options.get("rollMethod", gui.askRollMethod())
    filename = options.get("filename", None)
    count = options.get("count", None)
    if count is None:
        count = gui.askCharsCount()

    rooster = pathfinder.character.rooster.Rooster()
    rooster.load(filename)
    rooster.add(count=count)
    rooster.defineAbility()

    races = [random.choice(list(pathfinder.race.RACES.keys())) for i in rooster.chars]
    classes = [random.choice(list(pathfinder.charclass.CLASSES.keys())) for i in rooster.chars]

    logging.info("Pick Your Race")
    rooster.pickRace(races)
    logging.info("Pick Your Class")
    rooster.pickClass(classes)

    pickClass(rooster.chars, classes=[])
    pickSkills()
    buyEquipment()
    finishDetails()
    createChars(rooster)


if __name__ == "__main__":  # pragma: no cover
    import sys
    import getopt
    # import gui.commandline

    args = sys.argv[1:]
    try:
        parsed = gui.commandline.parseArgs(args)
    except(getopt.GetoptError):
        parsed = dict()
        gui.helpMessage()
    main(**parsed)
