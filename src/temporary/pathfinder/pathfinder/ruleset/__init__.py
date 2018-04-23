#! /usr/bin/env python
# -*- coding:utf-8 -*-


import dice


class Ruleset():
    def __init__(self, **args):
        from pathfinder.ruleset.level import NORMAL
        from pathfinder.ruleset.roll import STANDARD

        self.rollMethod = args.get("rollMethod", STANDARD)
        self.levelUp = args.get("levelUp", NORMAL)

    def rollAbility(self, ability, pool):
        ability.value = dice.d(**self.rollMethod)


rules = Ruleset()
