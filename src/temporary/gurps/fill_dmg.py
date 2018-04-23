def thrustDice(value):
    if value <= 10:
        return 1
    if value < 40:
        return (value - 11) // 8 + 1
    if value < 60:
        return (value - 5) // 10 + 1
    return (value) // 10 + 1


def thrustModifier(value):
    if value <= 10:
        return (value - 11) // 2 - 1
    if value < 40:
        return (value - 11) // 2 % 4 - 1
    if value < 60:
        return 1 + (value - 40) // 10 * 5 - (value - 40) // 5 * (value // 10 - 3)
    if value < 70:
        return (value - 60) // 5 * 2 - 1
    if value < 100:
        return (value - 60) // 5 % 2 * 2
    return 0


def swingDice(value):
    if value <= 10:
        return 1
    if value < 27:
        return (value - 9) // 4 + 1
    if value < 40:
        return (value - 7) // 8 + 3
    return (value) // 10 + 3


def swingModifier(value):
    if value < 9:
        return (value - 11) // 2
    if value < 27:
        return (value - 9) % 4 - 1
    if value < 40:
        g = (value - 9) // 2 + 1
        return g % 4 - 1
    if value < 60:
        return (value - 40) // 5 % 2 * 2 - 1
    if value < 100:
        return (value - 60) // 5 % 2 * 2
    return 0


def main():
    import attributes
    import db
    e, s = db.connect()

    s.query(attributes.BasicDamage).delete()
    s.commit()

    for st in range(1, 41):
        print("{}\t{}d + {}\t{}d + {}".format(st, thrustDice(st), thrustModifier(st), swingDice(st), swingModifier(st)))
        dmg = attributes.BasicDamage(
            st,
            [thrustDice(st), thrustModifier(st)],
            [swingDice(st), swingModifier(st)],
        )
        print(dmg)
        s.add(dmg)
    for st in range(45, 101, 5):
        print("{}\t{}d + {}\t{}d + {}".format(st, thrustDice(st), thrustModifier(st), swingDice(st), swingModifier(st)))
        dmg = attributes.BasicDamage(
            st,
            [thrustDice(st), thrustModifier(st)],
            [swingDice(st), swingModifier(st)],
        )
        print(dmg)
        s.add(dmg)
    s.commit()


if __name__ == "__main__":
    main()
