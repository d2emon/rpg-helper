#! /usr/bin/env python
# -*- coding:utf-8 -*-


def generate(args=[], nargs=dict()):
    STEPS = [
        "Determine Ability Scores",
        "Pick Your Race",
        "Pick Your Class",
        "Pick Skills and Select Feats",
        "Buy Equipment",
        "Finish Details",
    ]
    for i in range(len(STEPS)):
        print("{}. {}".format(i, STEPS[i]))
    print(args, nargs)
    return True
