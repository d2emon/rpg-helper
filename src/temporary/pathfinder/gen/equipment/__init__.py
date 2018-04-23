#! /usr/bin/env python
# -*- coding:utf-8 -*-


import logging


class EquipmentItem():
    def __init__(self):
        pass


ITEM_TYPES = {
    "craft": "z12",
    "component": "Spell component",
    "literature": "ad21",
    "vessel": "f30",
    "jewelry": "n24",
    "weapons": "d52",
    "cloth": "r34",
    "container": "Container t20\nar44",
    "figurine": "v17",
    "musical": "x13",

    "household": "ab22",
    "cutlery": "Cutlery",
    "dishes": "Dishware",
    "tapestry": "Tapestry",
    "travel": "aj10",
    "furniture": "p15",
    "painting": "Painting",
    "statue": "v18",
}


class ArtObject(EquipmentItem):
    TYPE_FILENAME = "../db/items/item_types.yml"
    CONDITION_FILENAME = "../db/items/conditions.yml"
    AGE_FILENAME = "../db/items/item_age.yml"
    PRICE_FILENAME = "../db/items/item_price.yml"

    def __init__(self):
        self.description = ""
        self.value = 0
        self.age = 0
        self.price_mod = 1

    def generatePerson(self):
        g = self.generate("person")
        print(g)

        item_type = g.get("type")
        it = ITEM_TYPES.get(item_type, item_type)
        condition = g.get("condition")
        self.description = "{} {}".format(condition, it)
        self.value = g.get("price", 0) * self.price_mod

    def generateCave(self):
        g = self.generate("cave")
        print(g)

        item_type = g.get("type")
        it = ITEM_TYPES.get(item_type, item_type)
        self.description = "A23"
        self.value = g.get("price", 0) * self.price_mod

    def generate(self, location):
        import random

        import yaml
        import dice

        p = ""
        c = ""

        data = dict()
        with open(self.TYPE_FILENAME) as f:
            data = yaml.load(f)
        logging.debug(location)
        logging.debug(data)
        l = data.get(location, {0: ""})
        p = dice.byPercent(l)

        data = dict()
        with open(self.CONDITION_FILENAME) as f:
            data = yaml.load(f)
        c = dice.byPercent(data)

        data = dict()
        with open(self.AGE_FILENAME) as f:
            data = yaml.load(f)
        age = dice.byPercent(data)

        data = dict()
        with open(self.PRICE_FILENAME) as f:
            data = yaml.load(f)
        price = random.randrange(*dice.byPercent(data))

        a = age.get("age", [1, 1])
        print(a)

        self.age = random.randrange(*age.get("age", [1, 1]))
        self.price_mod = c.get("mod", 1) * age.get("mod", 1)
        return {"type": p, "condition": c.get("name"), "price": price}


def main(id=0, options=[]):
    """
    Art Object generator main function
    """
    # import gui.menu
    logging.debug("Art Object generation")

    logging.debug(options)
    ao = ArtObject()
    ao.generatePerson()
    print("{} years old\n{}".format(ao.age, ao.value))
    print(ao.description)


if __name__ == "__main__":  # pragma: no cover
    import sys
    import getopt
    import gui
    import gui.commandline

    try:
        options = gui.commandline.parseArgs(sys.argv[1:])
    except(getopt.GetoptError):
        gui.helpMessage()

    main(options=options.get("args", []))
