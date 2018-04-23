def creationOrder():
    print("1.\tBase Attributes")
    print("2.\tBody")
    print("3.\tSocial")
    print("4.\tAdvantages")
    print("5.\tDisadvantages")
    print("6.\tSkills")


def showPC(pc):
    print(pc.name)
    for title, a in pc.attributes.items():
        print("{} {}[{}]\t{}\t{}".format(title, a.value, a.countCost(), a.valueDesc(), a.successRoll()))

    a = pc.attributes["ST"]
    print("Thrust {}d+{}\t[{}]".format(a.getThrustDice(), a.getTrustModifier(), a.thrust()))
    print("Swing  {}d+{}\t[{}]".format(a.getSwingDice(), a.getSwingModifier(), a.swing()))
    print("BL   {} p. = {} kg.\t{}/{}".format(a.BL(), a.BL()/2, a.pickUp(), a.liftHead()))
    print("HP   {}[{}]".format(pc.HP.getValue(), pc.HP.countCost()))
    print("Will {}[{}]".format(pc.Will.getValue(), pc.Will.countCost()))
    print("Perc {}[{}]".format(pc.Perc.getValue(), pc.Perc.countCost()))
    print("FP   {}[{}]".format(pc.FP.getValue(), pc.FP.countCost()))
    print("BS   {}[{}]\tDodge {}".format(pc.BS.getValue(), pc.BS.countCost(), pc.BS.dodge()))
    print("Move {}[{}]\t{} y/s = {} km/h".format(pc.Move.getValue(), pc.Move.countCost(), pc.Move.getValue(), pc.Move.getValue()))
    for i in range(4):
        print("load class({})".format(i))
        print("\tmax weight\t{}".format(pc.attributes["ST"].maxWeight(i)))
        print("\tmove\t{}".format(pc.BS.getValue() * pc.attributes["ST"].moveMdf(i)))
        print("\tdodge\t{}".format(pc.BS.dodge() + pc.attributes["ST"].dodgeMdf(i)))

    print("COST: {}".format(pc.countCost()))


def main():
    # import logging
    # logging.basicConfig(level=logging.DEBUG)

    creationOrder()

    import dice
    import pc
    import testPC

    p = pc.PlayerCharacter("Random")
    p.setST(dice.d(3))
    p.attributes["DX"].value = dice.d(3)
    p.attributes["IQ"].value = dice.d(3)
    p.attributes["HT"].value = dice.d(3)
    p.HP.modifier = dice.d(modifier=-3)
    p.Will.modifier = dice.d(modifier=-2)
    p.Perc.modifier = dice.d(modifier=-2)
    p.FP.modifier = dice.d(modifier=-3)
    p.BS.modifier = dice.d(modifier=-3)/4

    players = [
        pc.PlayerCharacter(),
        p,
        testPC.TestCharacter(),
    ]

    for pl in players:
        print("-"*80)
        showPC(pl)

    # print("{}({}): {}".format(p.ST.value, p.ST.valueDesc(), p.ST.countCost()))
    # print("{}({}): {}".format(p.DX.value, p.DX.valueDesc(), p.DX.countCost()))
    # print("{}({}): {}".format(p.IQ.value, p.IQ.valueDesc(), p.IQ.countCost()))
    # print("{}({}): {}".format(p.HT.value, p.HT.valueDesc(), p.HT.countCost()))

    print("-"*80)


if __name__ == "__main__":
    main()
