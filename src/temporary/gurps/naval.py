def NavalBattle(*ships):
    import dice
    bonuses = [0, 0]
    print(ships)
    if ships[0].maneuverability > ships[1].maneuverability:
        bonuses[0] = ships[0].maneuverability - ships[1].maneuverability
    else:
        bonuses[1] = ships[1].maneuverability - ships[0].maneuverability
    if ships[0].firepower > ships[1].firepower:
        if ships[1].firepower == 0:
            bonuses[0] = bonuses[0] + 8
        else:
            ratio = ships[0].firepower / ships[1].firepower
            bonuses[0] = bonuses[0] + ratio
    else:
        if ships[0].firepower == 0:
            bonuses[1] = bonuses[1] + 8
        else:
            ratio = ships[1].firepower / ships[0].firepower
            bonuses[1] = bonuses[1] + ratio

    for i in range(2):
        if i == 0:
            enemy = ships[1]
        else:
            enemy = ships[0]

        s = ships[i]
        print("-"*80)
        print(s.title)
        print("Maneuverability:\t{}({})".format(s.maneuverability, s.getManeuverabilityBonus(enemy)))
        if s.reinforced:
            print("Reinforced")
        print("Firepower:\t\t{}/{}({})".format(s.firepower, s.getFirepower(), s.getFirepowerBonus(enemy)))
        glory = s.getTotalGlory()
        print("Glory:\t\t\t{}".format(glory))
        bonus = s.getBonus(enemy)
        print("Bonus:\t\t\t{}".format(bonus))

        tacticRoll = dice.d(3)
        tacticRes = tacticRoll + s.getManeuverabilityBonus(enemy) + s.getFirepowerBonus(enemy) + bonus + glory

        print(bonuses[i])
        print(tacticRoll)
        print("Tactic: {}".format(tacticRoll))
        print(tacticRes)

    print("="*80)
    for ship in ships:
        print("{}({})".format(ship.title, ship.captain))
        ship.fight()


def main():
    import ship

    NavalBattle(
        ship.randomShip(),
        ship.Ship("ship2"),
    )


if __name__ == "__main__":
    main()
