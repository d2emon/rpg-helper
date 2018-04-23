#! /usr/bin/env python
# -*- coding:utf-8 -*-
from web import db


class Fraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, index=True, default="Фракция")
    description = db.Column(db.Unicode)
    weight = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Fraction {}>'.format(self.title)

    def avatar(self, size=32):
        from hashlib import md5
        title = self.title
        if title is None:
            import random
            title = repr(random.getrandbits(128))
        return "http://www.gravatar.com/avatar/" + md5(title.encode("utf-8")).hexdigest() + "?d=monsterid&s=" + str(size)
