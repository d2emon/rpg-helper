#! /usr/bin/env python
# -*- coding:utf-8 -*-


import logging
import yaml
import random

import gui.menu


WILDERNESS = [
    {"title": "Desolate/wasteland", "chance": 5},
    {"title": "Frontier/wilderness", "chance": 8},
    {"title": "Verdant/civilized", "chance": 10},
    {"title": "Heavily traveled", "chance": 12},
]
LAND_TYPES = []


class LandType():
    def __init__(self, data=""):
        pd = data.strip().rsplit("=")
        if len(pd) > 1:
            self.title = pd[1]
            self.groups = self.loadFromFile(pd[0])
        else:
            self.title = pd[0]
            self.groups = []

    def loadFromFile(self, filename):
        with open("../" + filename) as f:
            return yaml.load(f)

    def randomGroup(self):
        group = random.choice(self.groups)
        filename = group.get("file", None)
        if filename is not None:
            group.update(self.loadFromFile(filename))
        return group, random.choice(group["creatures"])


def getChance(wildernessType, hours=1):
    import dice
    try:
        for h in range(hours):
            w = WILDERNESS[wildernessType]
            r = dice.d(1, 100)
            enc = (r <= w["chance"])
            logging.debug("Hour: %d\tChance: %d\tRoll: %d\t%s" % (h, w["chance"], r, ["No encounter", "Encounter!"][enc]))
            if enc:
                break
        return h, enc
    except (IndexError):
        raise ValueError


def getCreatureType(landType):
    try:
        l = LAND_TYPES[landType]
    except (IndexError):
        raise ValueError
    g, c = l.randomGroup()
    print(l.title)
    return "%s(%s)" % (c, g["title"])


def action(action_id):
    return main()


def main(**options):
    global LAND_TYPES

    logging.basicConfig(level=logging.DEBUG)
    with open("../db/lands.dat") as f:
        LAND_TYPES = [LandType(s) for s in f.readlines()]
    while True:
        hs = gui.askHours()
        eh, ec = gui.menu.showMenu(items=[w["title"] for w in WILDERNESS], func=getChance, args={"hours": hs})
        print("You spent %d hours of %d" % (eh + 1, hs))
        if not ec and not gui.askYN("No encounter. Roll anyway?"):
            continue
        cg = gui.menu.showMenu(items=[l.title for l in LAND_TYPES], func=getCreatureType)
        print(cg)
        if not gui.askYN("Once again?"):
            gui.bye()


if __name__ == "__main__":
    main()
