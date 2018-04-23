#! /usr/bin/env python
# -*- coding:utf-8 -*-
from web import db


class GameCharacter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    charname = db.Column(db.String, index=True, default="Персонаж")
    description = db.Column(db.Unicode)
    st = db.Column(db.Integer, default=10)
    dx = db.Column(db.Integer, default=10)
    iq = db.Column(db.Integer, default=10)
    ht = db.Column(db.Integer, default=10)

    def __init__(self):
        db.Model.__init__(self)
        self.calcAttributes()

    def calcAttributes(self):
        import attributes
        self.ST = attributes.ST(self.st)
        self.DX = attributes.ST(self.dx)
        self.IQ = attributes.ST(self.iq)
        self.HT = attributes.ST(self.ht)

        self.HP = attributes.HP(self.ST)
        self.Will = attributes.Will(self.IQ)
        self.Perc = attributes.Perc(self.IQ)
        self.FP = attributes.FP(self.HT)
        self.BS = attributes.BS(self.DX, self.HT)
        self.Move = attributes.Move(self.BS)

    def __repr__(self):
        return '<Char {}>'.format(self.charname)

    def avatar(self, size=32):
        from hashlib import md5
        charname = self.charname
        if charname is None:
            import random
            charname = repr(random.getrandbits(128))
        return "http://www.gravatar.com/avatar/" + md5(charname.encode("utf-8")).hexdigest() + "?d=monsterid&s=" + str(size)
