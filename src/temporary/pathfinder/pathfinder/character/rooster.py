#! /usr/bin/env python
# -*- coding:utf-8 -*-


import logging
import yaml

import pathfinder.character


class Rooster():
    def __init__(self, **args):
        self.chars = args.get("chars", [])
        self.default = args.get("default", dict())

    def empty(self):
        self.chars = []

    def add(self, count=1, data=[], **default):

        charData = self.default.copy()
        charData.update(default)
        data = list(data) + [charData for i in range(len(data), count)]

        logging.debug("Loading: %s", data)
        [self.chars.append(pathfinder.character.Char(**d)) for d in data]
        return self.chars

    def load(self, filename=None):
        if filename is None:
            return self.chars

        with open(filename) as f:
            self.add(data=yaml.load(f))
        return self.chars

    def defineAbility(self, pool=None):
        logging.info("Determine Ability Scores")
        logging.debug("Rooster.defineAbility:Rules")
        for c in self.chars:
            logging.debug("%s's abilities", c.name)
            c.roll(pool)
        return self

    def pickRace(self, races=[]):
        for i, c in enumerate(self.chars):
            if i < len(races):
                raceId = races[i]
            else:
                raceId = i
            c.raceById(raceId)
            logging.debug("%s's race is %s(%d)", c.name, c.race.name, raceId)

    def pickClass(self, classes=[]):
        for i, c in enumerate(self.chars):
            if i < len(classes):
                classId = classes[i]
            else:
                classId = i
            c.favClass.append(classId)
            cl = c.classById(classId)
            logging.debug("%s's class is %s(%d)", c.name, cl.name, classId)
