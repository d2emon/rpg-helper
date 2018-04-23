#! /usr/bin/env python
# -*- coding:utf-8 -*-


import logging


SIZE_UNKNOWN = 0
SIZE_SMALL = 1
SIZE_MEDIUM = 2


SUBTYPE_GIANT = 1
SUBTYPE_ORC = 2
SUBTYPE_GOBLIN = 3
SUBTYPE_REPTILIAN = 4

MANEUVER_RUSH = 1
MANEUVER_TRIP = 2
MANEUVER_BONUS = 3
MANEUVER_DEFENSE = 4

SPELL_SLEEP = 1
SPELL_ENCHANT = 2
SPELL_ILLUSION = 3

UNKNOWN_ID = 0
HUMAN_ID = 1
DWARF_ID = 2
ELF_ID = 3
GNOME_ID = 4
HALFELF_ID = 5
HALFORC_ID = 6
HALFLING_ID = 7
ORC_ID = 8


def raceById(id):
    return RACES.get(id, Race)()


def raceHuman():
    import models.race
    r = models.race.Race()
    r.name = "Человек"
    r.custom_ability = 2
    r.bonus_feat = 1
    r.bonus_skill = 1
    return r


class Race():
    def __init__(self):
        self.name = "Unknown"
        self.blood = UNKNOWN_ID
        self.abilities = dict()
        self.randAbility = []
        self.size = SIZE_MEDIUM
        self.speed = 30
        self.lowlight = 1
        self.darkvision = 0
        self.favouredClasses = 1
        self.feats = []
        self.weapons = []
        self.weaponGroups = []
        self.languages = ["common"]
        self.additionalLanguages = []
        self.anyLanguage = False
        self.addFeat = 0
        self.addSkill = 0

    def apply(self, char):
        logging.debug("Race is %s", self.name)
        logging.debug("Before race: %s", char.abilities)
        for a in self.abilities.keys():
            char.abilities[a].value += self.abilities[a]
        logging.debug("After race: %s", char.abilities)

    def attack(self, enemy):
        if self.size == SIZE_SMALL:
            return 1
        return 0

    def dodge(self, enemy):
        return 0

    def maneuver(self, maneuver, ground=False):
        if self.size == SIZE_MEDIUM:
            if (maneuver == MANEUVER_BONUS) or (maneuver == MANEUVER_DEFENSE):
                return -1
        return 0

    def perception(self, stone=False):
        return 0

    def notice(self, dist=0):
        return False

    def skill(self, skillName, identify=False):
        if self.size == SIZE_SMALL:
            if skillName == "stealth":
                return 4
        return 0

    def spell(self, spellType=0):
        return 0

    def overcome(self):
        return 0

    def ac(self):
        if self.size == SIZE_SMALL:
            return 1
        return 0

    def fear(self):
        return 0

    def savingThrow(self):
        return 0


class Human(Race):
    def __init__(self):
        Race.__init__(self)
        self.name = "Human"
        self.blood = [HUMAN_ID]
        self.randAbility = [2]

        self.addFeat = 1
        self.addSkill = 1

        self.anyLanguage = True

    def perception(self, stone=False):
        return 2

    def spell(self, spellType=0):
        if spellType == SPELL_SLEEP:
            return None
        if spellType == SPELL_ENCHANT:
            return 2
        return 0


class Dwarf(Race):
    def __init__(self):
        Race.__init__(self)
        self.name = "Dwarf"
        self.blood = [DWARF_ID]
        self.abilities = {"CON": 2, "WIS": 2, "CHA": -2}
        self.speed = 20
        self.darkvision = 60
        self.weapons = ["battleaxe", "heavy pick", "warhammer"]
        self.weaponGroups = ["dwarven"]
        self.languages.append("dwarven")
        self.additionalLanguages = ["giant", "gnome", "goblin", "orc", "terran", "undercommon"]

    def attack(self, enemy):
        mod = Race.attack(self, enemy)
        if enemy in (SUBTYPE_ORC, SUBTYPE_GOBLIN):
            return mod + 1
        return mod

    def dodge(self, enemy):
        if enemy == SUBTYPE_GIANT:
            return 4
        return 0

    def maneuver(self, maneuver, ground=False):
        mod = Race.maneuver(self, maneuver)
        if ground:
            if maneuver in (MANEUVER_RUSH, MANEUVER_TRIP):
                return 4 + mod
        return mod

    def perception(self, stone=False):
        if stone:
            return 2
        return 0

    def notice(self, dist=0, stone=False):
        if dist <= 0:
            return False
        if dist <= 10:
            return stone
        return False

    def skill(self, skillName, identify=False):
        mod = Race.maneuver(self, skillName, identify)
        if skillName == "Appraise":
            return 2 + mod
        elif skillName == "Stealth":
            if self.size == SIZE_SMALL:
                return 4 + mod
        return mod


class Elf(Race):
    def __init__(self):
        Race.__init__(self)
        self.name = "Elf"
        self.blood = [ELF_ID]
        self.abilities = {"DEX": 2, "INT": 2, "CON": -2}
        self.lowlight = 2
        self.weapons = ["longbow", "longsword", "rapier", "shortbow"]
        self.weaponGroups = ["elven"]
        self.languages.append("elven")
        self.additionalLanguages = ["celestial", "draconic", "gnoll", "gnome", "goblin", "orc", "sylvan"]

    def perception(self, stone=False):
        return 2

    def skill(self, skillName, identify=False):
        mod = Race.skill(self, skillName, identify)
        if skillName == "Spellcraft":
            if identify:
                return 2 + mod
        return mod

    def spell(self, spellType=0):
        if spellType == SPELL_SLEEP:
            return None
        if spellType == SPELL_ENCHANT:
            return 2
        return 0

    def overcome(self):
        return 2


class Gnome(Race):
    def __init__(self):
        Race.__init__(self)
        self.name = "Gnome"
        self.blood = [GNOME_ID]
        self.abilities = {"CON": 2, "CHA": 2, "STR": -2}
        self.size = SIZE_SMALL
        self.speed = 20
        self.lowlight = 2

        self.weaponGroups = ["gnome"]
        self.languages += ["gnome", "sylvan"]
        self.additionalLanguages = ["draconic", "dwarven", "elven", "giant", "goblin", "orc"]

    def attack(self, enemy):
        mod = Race.attack(self, enemy)
        if enemy in (SUBTYPE_REPTILIAN, SUBTYPE_GOBLIN):
            return mod + 1
        return mod

    def dodge(self, enemy):
        if enemy == SUBTYPE_GIANT:
            return 4
        return 0

    def spellike(self, char):
        if char.abilities["CHA"] >= 11:
            spellike = ["dancing lights", "ghost sound", "prestidigitation", "speak with animals"]
            return [{"name": s, "daily": 1, "level": char.level, "dc": 10 + char.level + char.abilities["CHA"].modifier} for s in spellike]

    def spell(self, spellType=0):
        if spellType == SPELL_ILLUSION:
            return 1
        return 0

    def skill(self, skillName, identify=False):
        mod = Race.skill(self, skillName, identify)
        if skillName in ("Perception", "Craft", "Profession"):
            return 2 + mod
        return mod


class Halfelf(Human):
    def __init__(self):
        Race.__init__(self)
        self.name = "Halfelf"
        self.blood = [HALFELF_ID, ELF_ID, HUMAN_ID]
        self.lowlight = 2
        self.feats = ["skillFocus"]
        self.favouredClasses = 2

        self.languages.append("elven")
        self.anyLanguage = True

        self.addFeat = 0
        self.addSkill = 0

    def perception(self, stone=False):
        return 2

    def spell(self, spellType=0):
        if spellType == SPELL_SLEEP:
            return None
        if spellType == SPELL_ENCHANT:
            return 2
        return 0


class Halforc(Human):
    def __init__(self):
        Race.__init__(self)
        self.name = "Halforc"
        self.blood = [HALFORC_ID, ORC_ID, HUMAN_ID]
        self.darkvision = 60

        self.weapons = ["greataxe", "falchion"]
        self.weaponGroups = ["orc"]
        self.languages.append("orc")
        self.additionalLanguages = ["abyssal", "draconic", "giant", "gnoll", "goblin"]

        self.anyLanguage = False
        self.addFeat = 0
        self.addSkill = 0

        self.ferocityDay = 1

    def skill(self, skillName, identify=False):
        mod = Race.skill(self, skillName, identify)
        if skillName == "Intinidate":
            return 2 + mod
        return mod

    def ferocity(self, hp=0, killed=False):
        if hp >= 0:
            return False
        if killed:
            return False
        self.ferocityDay -= 1
        return {"disabled": True, "round": 1, "after": {"unconscious": True, "dying": True}}


class Halfling(Race):
    def __init__(self):
        Race.__init__(self)
        self.name = "Halfling"
        self.blood = [HALFLING_ID]
        self.abilities = {"DEX": 2, "CHA": 2, "STR": -2}
        self.size = SIZE_SMALL
        self.speed = 20

        self.weapons = ["slings"]
        self.weaponGroups = ["halfling"]
        self.languages.append("halfling")
        self.additionalLanguages = ["dwarven", "elven", "ginome", "goblin"]

    def fear(self):
        return 2

    def savingThrow(self):
        return 1

    def perception(self, stone=False):
        return 2

    def skill(self, skillName, identify=False):
        mod = Race.skill(self, skillName, identify)
        if skillName in ("Acrobatics", "Climb"):
            return 2 + mod
        return mod


RACES = {
    HUMAN_ID: Human,
    DWARF_ID: Dwarf,
    ELF_ID: Elf,
    GNOME_ID: Gnome,
    HALFELF_ID: Halfelf,
    HALFORC_ID: Halforc,
    HALFLING_ID: Halfling,
}
