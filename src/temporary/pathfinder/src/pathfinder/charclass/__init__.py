#! /usr/bin/env python
# -*- coding:utf-8 -*-


import pathfinder.ruleset
import pathfinder.charclass.baseclass
import pathfinder.charclass.fighter


class Level():
    def __init__(self, level=0):
        self.level = level

    def toNext(self):
        return pathfinder.ruleset.rules.levelUp[self.level]

    def getFeat(self):
        return (self.level % 2) == 1

    def getSkill(self):
        return True

    def getAbility(self):
        return (self.level % 4) == 0

    feat = property(getFeat)
    skill = property(getSkill)
    ability = property(getAbility)


def xpToLevel(xp):
    for l, tolup in enumerate(pathfinder.ruleset.rules.levelUp):
        if xp < tolup:
            return Level(l)


UNSET_ID = -1
UNKNOWN_ID = 0


def classById(id):
    return CLASSES.get(id, pathfinder.charclass.baseclass.CharClass)()


from pathfinder.charclass.fighter import BRB_ID
from pathfinder.charclass.fighter import Barbarian


CLASSES = {
    BRB_ID: Barbarian,
}
