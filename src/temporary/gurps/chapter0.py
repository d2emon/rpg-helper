import dice



def successRoll(skill, modifier=0):
    modified = skill + modifier
    roll = dice.d(3)

    import logging
    logging.debug("%d vs. %d [%d(%d)]", roll, modified, skill, modifier)
    return roll <= modified


def reactRoll(modifier=0):
    roll = dice.d(3, modifier=modifier)
    return roll


def damageRoll(skill, modifier=0):
    modified = skill + modifier
    roll = dice.d(3)

    import logging
    logging.debug("%d vs. %d [%d(%d)]", roll, modified, skill, modifier)
    return roll <= modified


def main():
    print("Success roll:\t{}".format(successRoll(12, -2)))
    print("React roll:\t{}".format(reactRoll(-2)))
    print("Damage roll:\t{}".format(damageRoll(12, -2)))


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    main()
