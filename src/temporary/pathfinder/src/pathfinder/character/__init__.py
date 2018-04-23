#! /usr/bin/env python
# -*- coding:utf-8 -*-


import logging
import pathfinder.ruleset
import pathfinder.abilities
import pathfinder.race
import pathfinder.charclass

from pathfinder.character import gender


STATS = {
    "STR": {"class": pathfinder.abilities.Ability, "dices": 3},
    "DEX": {"class": pathfinder.abilities.Ability, "dices": 3},
    "CON": {"class": pathfinder.abilities.Ability, "dices": 3},
    "INT": {"class": pathfinder.abilities.SpellAbility, "dices": 3},
    "WIS": {"class": pathfinder.abilities.Ability, "dices": 3},
    "CHA": {"class": pathfinder.abilities.Ability, "dices": 3},
}

VISION = {
    "normal": True,
    "low": 1,
    "dark": 0,
}


class Char():
    default = {
        "name": "Unnamed",
        "player": "Unknown",
        "alignment": None,
        "race": None,
        "favClass": [],
        "deity": "Unknown",
        "homeland": "Homeland",
        "size": 0,
        "gender": gender.UNKNOWN_ID,
        "age": 0,
        "height": 0,
        "weight": 0,
        "hair": "Unknown",
        "eyes": "Unknown",
        "hp": 0,
        "initiative": 0,
        "speed": 0,
        "skills": [],
        "ac": 0,
        "savingThrows": [],
        "bab": 0,
        "spellResistance": 0,
        "cmb": 0,
        "cmd": 0,
        "weapons": [],
        "languages": [],
    }

    def __init__(self, **args):
        logging.debug("Character data are: %s", args)

        self.abilities = {s: d["class"]() for s, d in STATS.items()}
        self.vision = args.get("vision", VISION.copy())
        self.resetClasses()

        for a in self.default:
            setattr(self, a, args.get(a, self.default[a]))

        stats = args.get("stats", dict())
        logging.debug("Stats are: %s", stats)
        self.fill(**stats)

        # rollPool = args.get("rollPool", None)
        # if rollPool is None:
        #     rollPool = {s: d["dices"] for s, d in STATS.items()}
        # self.roll(rollPool)

        self.raceById(args.get("raceId", pathfinder.race.UNKNOWN_ID))
        self.classById(args.get("classId", pathfinder.charclass.UNSET_ID))

    def roll(self, pool=None):
        [pathfinder.ruleset.rules.rollAbility(a, pool) for a in self.abilities.values()]

    def fill(self, **named):
        for i, a in enumerate(named):
            self.abilities[a].value = named[a]
        logging.debug("Abilities are: %s", self.abilities)

    def raceById(self, id):
        r = pathfinder.race.raceById(id)
        logging.debug(r.name)
        self.race = r
        return r

    def classById(self, id, level=1):
        if id == pathfinder.charclass.UNSET_ID:
            return None
        c = pathfinder.charclass.classById(id)
        logging.debug(c.name)
        favoured = c.id in self.favClass
        self.charClass[c.id] = {"class": c, "level": level, "favoured": favoured}
        return c

    def resetClasses(self):
        self.charClass = dict()

    def getCost(self):
        stats = [s.cost for s in self.abilities.values()]
        logging.debug("Character cost is %d(%s)", sum(stats), " + ".join([str(s) for s in stats]))
        return sum(stats)

    def getRace(self):
        return self.__race

    def setRace(self, value):
        if value is None:
            value = pathfinder.race.Race()

        self.__race = value
        for i, a in self.abilities.items():
            a.racialAdjustment = value.abilities.get(i, 0)

        logging.debug("Race Vv:%s", self.vision)
        self.vision["low"] = value.lowlight
        self.vision["dark"] = value.darkvision
        logging.debug("Race Vv:%s", self.vision)

    def getFavClass(self):
        return self.__favClass

    def setFavClass(self, value):
        if value is None:
            return

        maxClasses = self.race.favouredClasses - 1
        del value[:maxClasses]
        self.__favClass = value

    def getCharClass(self):
        return self.__charClass

    def setCharClass(self, value):
        self.__charClass = value
        if value is None:
            return

        logging.debug("V:%s", value)
        logging.debug("Vv:%s", self.vision)

    cost = property(getCost)
    race = property(getRace, setRace)
    charClass = property(getCharClass, setCharClass)
