from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Unicode

Base = declarative_base()

import attributes


class BasicDamage(Base):
    __tablename__ = 'basic_damage'
    id = Column(Integer, primary_key=True)
    value = Column(Integer, default=10)
    thrust_dice = Column(Integer)
    thrust_mod = Column(Integer)
    swing_dice = Column(Integer)
    swing_mod = Column(Integer)

    def __init__(self, value, thrust=[1, -2], swing=[1, 0]):
        self.value = value
        self.thrust_dice, self.thrust_mod = thrust
        self.swing_dice, self.swing_mod = swing

    def __repr__(self):
        return "<ST({})\tthrust {}d+{}\tswing {}d+{}>".format(self.value,
                                                                self.thrust_dice, self.thrust_mod,
                                                                self.swing_dice, self.swing_mod)

    def thrust(self):
        return self.thrust_dice, self.thrust_mod

    def swing(self):
        return self.swing_dice, self.wing_mod


class Attribute:
    defValue = 10
    cost = 10

    def __init__(self, value=None):
        if value is not None:
            self.value = value
        else:
            self.value = self.defValue

    def __repr__(self):
        return "[{}]".format(self.value)

    def getValue(self):
        return self.value

    def valueDesc(self):
        if self.value <= 6:
            return "Cripping"
        if self.value <= 7:
            return "Low"
        if self.value <= 9:
            return "Below Average"
        if self.value <= 10:
            return "Normal"
        if self.value <= 12:
            return "Above Average"
        if self.value <= 14:
            return "Excellent"
        return "Unbeliveable"

    def countCost(self):
        delta = self.value - self.defValue
        return delta * self.cost

    def successRoll(self, modifier=0):
        modified = self.value + modifier

        import dice
        roll = dice.d(3)

        import logging
        logging.debug("%d vs. %d [%d(%d)]", roll, modified, self.value, modifier)
        return roll <= modified


class ST(Attribute):
    cost = 10

    def damage(self):
        import db
        e, s = db.connect()
        return s.query(BasicDamage).filter(BasicDamage.value >= self.value).order_by(BasicDamage.value.asc()).first()

    def thrust(self):
        dmg = self.damage()
        print(dmg)
        dices, mod = dmg.thrust()

        import dice
        return dice.d(dices, modifier=mod)

    def swing(self):
        dmg = self.damage()
        print(dmg)
        dices, mod = dmg.thrust()

        import dice
        return dice.d(dices, modifier=mod)

    def BL(self):
        BL = self.value * self.value / 5

        if BL > 10:
            return int(BL)
        return BL

    def pickUp(self):
        return self.BL() * 2

    def liftHead(self):
        return self.BL() * 8

    def maxWeight(self, loadClass):
        return self.BL() * (1 + loadClass * loadClass)

    def moveMdf(self, loadClass):
        return 1 - loadClass * 0.2

    def dodgeMdf(self, loadClass):
        return -loadClass


class DX(Attribute):
    cost = 20


class IQ(Attribute):
    cost = 20


class HT(Attribute):
    cost = 10


class Secondary(Attribute):
    def __init__(self, Primary, modifier=0):
        Attribute.__init__(self, value=Primary.getValue() + modifier)

        self.Primary = Primary
        self.modifier = modifier

    def getValue(self):
        return self.Primary.getValue() + self.modifier

    def countCost(self):
        return self.modifier * self.cost


class HP(Secondary):
    cost = 2


class Will(Secondary):
    cost = 5


class Perc(Secondary):
    cost = 5


class FP(Secondary):
    cost = 3


class BS(Attribute):
    cost = 20

    def __init__(self, DX=None, HT=None, modifier=0):
        Attribute.__init__(self, value=(DX.value + HT.value) / 4 + modifier)

        self.Primaries = [DX, HT]
        self.modifier = modifier

    def getValue(self):
        s = 0
        for i in self.Primaries:
            s += i.value
        return s / 4 + self.modifier

    def countCost(self):
        return self.modifier * self.cost

    def dodge(self):
        return int(self.getValue()) + 3


class Move(Secondary):
    cost = 5

    def getValue(self):
        return int(self.Primary.getValue()) + self.modifier
