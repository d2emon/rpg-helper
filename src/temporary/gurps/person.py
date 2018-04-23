class Person:
    pass


class Weapon:
    onMovePenalty = 0
    closeCombat = False

    def getCloseCombatModifier(self):
        if self.closeCombat:
            return 0
        else:
            return -2


class Bow(Weapon):
    onMovePenalty = 6


class Crossbow(Weapon):
    onMovePenalty = 3


class Knife(Weapon):
    closeCombat = True


class Position:
    title = "UNNAMED"
    attack = 0
    defense = ""
    movement = 1
    movementMod = 0.0


class Standing(Position):
    title = "Standing"


class Crouching(Position):
    title = "Crouching"
    attack = -2
    defense = "Ranged weapons -2 to hit you; normal vs. others"
    movementMod = 0.5


class Attacker(Person):
    mainHand = True
    movement = 0
    familiarity = True

    def __init__(self):
        import cards

        self.weaponSkill = 10
        self.weapon = Weapon()
        self.card = cards.Nothing()
        self.position = Standing()

    def getOnMove(self):
        if self.movement < 1:
            penalty = 0
        else:
            penalty = -self.movement

        return penalty * self.weapon.onMovePenalty

    def getHandPenalty(self):
        if self.mainHand:
            return -4
        return 0

    def familiarWeapon(self, weapon=None):
        if weapon is None:
            weapon = self.weapon

        if self.familiarity:
            return 0
        else:
            return -2

    def getWildSwing(self):
        if self.card.isWildSwing():
            return -5
        else:
            return 0

    def getPersonalCombatModifier(self):
        print("\tOn move:\t{}".format(self.getOnMove()))
        print("\tHandness:\t{}".format(self.getHandPenalty()))
        print("\tFamiliar wpn:\t{}".format(self.familiarWeapon()))
        print("\tHit bonus:\t{}".format(self.card.getHitBonus()))
        print("\tWild swing:\t{}".format(self.getWildSwing()))
        print("\tClose combat:\t{}".format(self.weapon.getCloseCombatModifier()))
        print("\tPosition:\t{}".format(self.position.attack))

        bonus = self.getOnMove() + self.getHandPenalty() + self.familiarWeapon()
        bonus = bonus + self.card.getHitBonus() + self.getWildSwing()
        bonus = bonus + self.weapon.getCloseCombatModifier() + self.position.attack
        print("\tPersonal Bonus:\t{}".format(bonus))
        return bonus
