from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Unicode
from sqlalchemy import event

Base = declarative_base()

import attributes


class PlayerCharacter(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Unicode)
    st = Column(Integer, default=10)
    dx = Column(Integer, default=10)
    iq = Column(Integer, default=10)
    ht = Column(Integer, default=10)

    def __init__(self, name="UNNAMED"):
        self.name = name
        self.addAttributes()

        self.HP = attributes.HP(self.ST)
        self.Will = attributes.Will(self.IQ)
        self.Perc = attributes.Perc(self.IQ)
        self.FP = attributes.FP(self.HT)
        self.BS = attributes.BS(self.DX, self.HT)
        self.Move = attributes.Move(self.BS)

        # self.st = self.ST.value
        # self.dx = self.DX.value
        # self.iq = self.IQ.value
        # self.ht = self.HT.value

    def __repr__(self):
        return "<User#{}\t'{}'>".format(self.id, self.name)

    def setST(self, value):
        self.ST.value = value

    def setDX(self, value):
        self.DX.value = value

    def setIQ(self, value):
        self.IQ.value = value

    def setHT(self, value):
        self.HT.value = value

    def countCost(self):
        cost = 0
        for title, a in self.attributes.items():
            cost += a.countCost()
        cost += self.HP.countCost()
        cost += self.Will.countCost()
        cost += self.Perc.countCost()
        cost += self.FP.countCost()
        return cost

    def addAttributes(self):
        self.ST = attributes.ST()
        self.DX = attributes.DX()
        self.IQ = attributes.IQ()
        self.HT = attributes.HT()

    def beforeSave(self):
        self.st = self.ST.getValue()
        self.dx = self.DX.getValue()
        self.iq = self.IQ.getValue()
        self.ht = self.HT.getValue()

    def afterLoad(self):
        self.addAttributes()

        self.setST(self.st)
        self.setDX(self.dx)
        self.setIQ(self.iq)
        self.setHT(self.ht)


@event.listens_for(PlayerCharacter, 'before_insert')
@event.listens_for(PlayerCharacter, 'before_update')
def receive_before_insert(mapper, connection, target):
    print("INSERT")
    print(mapper)
    print(connection)
    print(target)


# event.listen(PlayerCharacter, 'before_insert', receive_before_insert)
# event.listen(PlayerCharacter, 'before_update', receive_before_insert)


def save(pc, session):
    pc.beforeSave()
    print("BEFORE SAVE")
    session.add(pc)
    session.flush()
    # session.commit()
    print("+"*80)


def load(session, id):
    c = session.query(PlayerCharacter).filter_by(id=id).one()
    c.addAttributes()
    return c