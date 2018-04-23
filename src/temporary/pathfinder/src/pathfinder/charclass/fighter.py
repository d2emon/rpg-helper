#! /usr/bin/env python
# -*- coding:utf-8 -*-


from pathfinder.charclass.baseclass import CharClass


BRB_ID = 101


class Barbarian(CharClass):
    def __init__(self):
        CharClass.__init__(self)
        self.id = BRB_ID
        self.name = "Barbarian"
        self.alignments = [(x, y) for x in range(-1, 0) for y in range(-1, 1)]
        self.hd = (1, 12)
        self.skills = [
            "Acrobatics",
            "Climb",
            "Craft",
            "HandleAnimal",
            "Intimidate",
            "Knowledge",
            "Perception",
            "Ride",
            "Survival",
            "Swim",
        ]
        self.skillRanks = 4
        self.weaponProficiency = ["simple", "martial"]
        self.armorProficiency = ["light", "medium"]
        self.shieldProficiency = ["shields"]
        self.ex = [
            self.fastMove,
            self.rage,
            self.ragePower,
            self.uncannyDodge,
            self.trapSense,
            self.ragePower,
            self.uncannyDodge,
            self.damageReduction,
            self.indomitableWill,
        ]

    def bab(self, level):
        return [level - (5 * i) for i in range(level / 5)]

    def fort(self, level):
        return int(level / 2) + 2

    def ref(self, level):
        return int(level / 3)

    def will(self, level):
        return int(level / 3)

    def fastMove(self):
        pass

    def rage(self):
        pass

    def ragePower(self):
        pass

    def uncannyDodge(self):
        pass

    def trapSense(self):
        pass

    def improvedUncannyDodge(self):
        pass

    def damageReduction(self):
        pass

    def indomitableWill(self):
        pass
