#! /usr/bin/env python
# -*- coding:utf-8 -*-


from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

    
class Line:
    def __init__(self, s=""):
        self.data = s.strip()  # .encode('utf-8')


def LinesFile(filename):
    lines = []
    with open(filename, encoding='utf-8') as f:
        lines = [Line(s) for s in f.readlines()]
        return(lines)


def get_random_line(lines):
    import random
    random.shuffle(lines)
    return lines[0]


def get_RussianName(male=True):
    if male:
        nm1 = LinesFile("db/names/russian/names1-m.txt")
        nm2 = LinesFile("db/names/russian/names2-m.txt")
        nm3 = LinesFile("db/names/russian/names3-m.txt")
    else:
        nm1 = LinesFile("db/names/russian/names1-f.txt")
        nm2 = LinesFile("db/names/russian/names2-f.txt")
        nm3 = LinesFile("db/names/russian/names3-f.txt")
    return get_random_line(nm1).data + " " + get_random_line(nm2).data + " " + get_random_line(nm3).data