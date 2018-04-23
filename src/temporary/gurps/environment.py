class Environment:
    modifier = 0
    footing = True
    darkness = 0

    def getCombatModifier(self):
        return self.modifier + self.getFooting() + self.getDarkness()

    def getFooting(self):
        if self.footing:
            return 0
        else:
            return -2

    def getDarkness(self):
        if self.darkness < 0:
            return 0
        return -self.darkness

    def report(self):
        if self.darkness <= 0:
            print("Light")
        else:
            print("Darkness({})".format(self.darkness))
        if not self.footing:
            print("Bad Footing")
        print("Modifier: {}".format(self.getCombatModifier()))
