class Crewman:
    gloryMod = [3, 2, 1, 0, -1, -2, -3]

    def __init__(self, **params):
        self.glory = params.get("glory", 0)
        self.battle = params.get("battle", 10)
        self.active = params.get("active", False)

    def getGloryRoll(self):
        import dice
        roll = dice.d(6)
        if roll > 17:
            print("Glory Roll Critical Success")
            return self.gloryMod[0]
        if roll <= 3:
            print("Glory Roll Critical Failure")
            return self.gloryMod[6]

        print("Rolled:\t{} + {}".format(roll, self.glory))
        roll += self.glory
        if roll >= 10:
            return self.gloryMod[0]
        if roll >= 7:
            return self.gloryMod[1]
        if roll >= 4:
            return self.gloryMod[2]
        if roll >= 0:
            return self.gloryMod[3]
        if roll >= -3:
            return self.gloryMod[4]
        if roll >= -6:
            return self.gloryMod[5]
        return self.gloryMod[6]

    def gloryRoll(self):
        if self.active:
            return self.getGloryRoll()
        else:
            return int(self.getGloryRoll() / 3)


class Captain(Crewman):
    gloryMod = [5, 4, 2, 0, -2, -4, -5]

    def __init__(self, **params):
        Crewman.__init__(self, **params)
        self.tactics = params.get("tactics", 10)
        self.active = True


class Ship:
    surpriseBonus = [0, 2, 5]

    def __init__(self, title="Ship", **params):
        self.title = title
        print(params)
        self.captain = params.get("captain", Captain())
        self.maneuverability = params.get("maneuverability", -4)
        self.reinforced = params.get("reinforced", False)
        self.firepower = params.get("firepower", 100)
        self.bonus = params.get("bonus", 0)
        self.speed = params.get("speed", 10)
        self.surprise = params.get("surprise", 0)
        self.familiar = params.get("familiar", 0)
        self.home = params.get("home", False)
        self.wind = params.get("wind", False)
        self.crewLevel = params.get("crewLevel", 0)

        self.crew = [self.captain, ]

        for m in params.get("crew", []):
            self.crew.append(m)

    def getBonus(self, enemy):
        bonus = 0
        if self.speed - enemy.speed >= 2:
            bonus += 1
        bonus += self.surpriseBonus[self.surprise]
        bonus += self.familiar
        if self.home:
            bonus += 2
        if self.wind:
            bonus += 2
        bonus += self.crewLevel * 2
        return bonus

    def getTactic(self):
        return self.captain.tactics

    def getTotalGlory(self):
        totalGlory = 0
        for c in self.crew:
            glory = c.gloryRoll()
            totalGlory += glory
            print("Crewman {}".format(c))
            if c.active:
                print("Active")
            else:
                print("Passive")
                print("Glory: {}".format(glory))
        return totalGlory

    def getManeuverabilityBonus(self, enemy):
        if enemy.maneuverability > self.maneuverability:
            return 0
        return self.maneuverability - enemy.maneuverability

    def getFirepower(self):
        firepower = self.firepower
        if self.reinforced:
            firepower += int(self.firepower * 0.25)
        return firepower

    def getFirepowerBonus(self, enemy):
        if self.getFirepower() <= 0:
            return 0
        if enemy.getFirepower() > self.getFirepower():
            return 0
        if enemy.getFirepower() <= 0:
            return 8
        ratio = self.getFirepower() / enemy.getFirepower()
        if ratio <= 1.2:
            return 0
        if ratio <= 1.4:
            return 1
        if ratio <= 1.7:
            return 2
        if ratio <= 2.0:
            return 3
        if ratio <= 3.0:
            return 4
        if ratio <= 5.0:
            return 5
        if ratio <= 7.0:
            return 6
        if ratio <= 10.0:
            return 7
        return 8

    def fight(self):
        import dice

        tacticLevel = self.getTactic()
        tacticRoll = dice.d(3)
        print("Tactic {} vs {}".format(tacticRoll, tacticLevel))


def randomShip():
    import random
    s = Ship("Random Ship",
             captain=Captain(tactics=random.randint(0, 20)),
             maneuverability=random.randrange(-6, -1),
             firepower=random.randint(0, 700),
             reinforced = (random.randrange(0, 2) > 0),
             speed=random.randrange(10, 100),
             surprise=random.randrange(0, 3),
             familiar=random.randrange(0, 4),
             home=(random.randrange(0, 2) > 0),
             wind=(random.randrange(0, 2) > 0),
             crewLevel=random.randrange(-1, 2),
             )
    crewCount = random.randrange(1, 10)
    for i in range(crewCount):
        s.crew.append(Crewman(
            battle = random.randrange(0, 20),
            glory = random.randrange(-6, 6),
            active = (random.randrange(0, 2) > 0)
        ))
    return s
