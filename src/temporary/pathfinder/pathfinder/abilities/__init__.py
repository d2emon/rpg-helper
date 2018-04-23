#! /usr/bin/env python
# -*- coding:utf-8 -*-


class Ability():
    minValue = 3
    maxValue = 18

    def __init__(self, value=None):
        self.value = value
        self.tempAdjustment = 0
        self.racialAdjustment = 0

    @property
    def value(self):
        return self.__value + self.racialAdjustment + self.tempAdjustment

    @value.setter
    def value(self, value):
        self.isSet = value is not None

        if not self.isSet:
            value = 0

        if value < self.minValue:
            self.__value = self.minValue
        elif value > self.maxValue:
            self.__value = self.maxValue
        else:
            self.__value = value

    def getCost(self):
        if self.value > 16:
            return 4 * (self.value - 14) + 1
        elif self.value > 14:
            return 3 * (self.value - 13) + 1
        elif self.value > 12:
            return 2 * (self.value - 12) + 1
        elif self.value > 7:
            return (self.value - 11) + 1
        else:
            return -4

    def getModifier(self):
        return int(self.value / 2) - 5

    def __str__(self):
        return "%s(%d)%s" % (["Not set", self.value][self.isSet], self.modifier, (self.__value, self.racialAdjustment, self.tempAdjustment))

    def __repr__(self):
        return self.__str__()

    cost = property(getCost)
    modifier = property(getModifier)


class SpellAbility(Ability):
    def getSpells(self):
        m = self.modifier
        spells = [[0, int((m - i - 1) / 4) + 1][i < m] for i in range(9)]
        return [0] + spells

    def canSpell(self):
        return self.value >= 10

    def __str__(self):
        return super(SpellAbility, self).__str__() + ":%s" % (["-", self.spells][self.canSpell()])

    spells = property(getSpells)
