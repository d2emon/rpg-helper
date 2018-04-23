#! /usr/bin/env python
# -*- coding:utf-8 -*-


def showChar(char):
    print("Name:\t", char.name)
    print("Align:\t", char.alignment)
    print("Player:\t", char.player)
    showClass(char)
    print("Deity:\t", char.deity)
    print("Home:\t", char.homeland)
    showRace(char)
    print("Size:\t", char.size)
    print("Gender:\t", ["?", "M", "F"][char.gender])
    print("Age:\t", char.age)
    print("Height:\t", char.height)
    print("Weight:\t", char.weight)
    print("Hair:\t", char.hair)
    print("Eyes:\t", char.eyes)
    showAbilities(char)
    print("-" * 40)
    print("Cost:\t", char.cost)


def showAbilities(char):
    for k in char.abilities:
        a = char.abilities[k]
        print("\t%s:\t%s" % (k, a))


def showRace(char):
    race = char.race
    print("Race:\t%s" % (race.name))
    print("\tVision: %s (Lowlight: %d, Darkvision: %d ft)" % (char.vision["normal"], char.vision["low"], char.vision["dark"]))
    print("\tAbilities: ", race.abilities)
    print("\tSize: ", race.size)
    print("\tSpeed: ", race.speed)
    print("\tLowlight: ", race.lowlight)
    print("\tDarkvision: ", race.darkvision)
    print("\tWeapons: ", race.weapons, race.weaponGroups)
    print("\tLanguages: ", race.languages, race.additionalLanguages)


def showClass(char):
    print("Classes:\t")
    for c in char.charClass.values():
        print("\t%s(%d)%s" % (c["class"].name, c["level"], ["", "*"][c["favoured"]]))
