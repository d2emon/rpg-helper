#! /usr/bin/env python
# -*- coding:utf-8 -*-


import pathfinder.charclass


class CharClass():
    def __init__(self):
        self.id = pathfinder.charclass.UNKNOWN_ID
        self.name = "Unknown"
        self.alignments = [(x, y) for x in range(-1, 1) for y in range(-1, 1)]
        self.hd = (1, 8)
