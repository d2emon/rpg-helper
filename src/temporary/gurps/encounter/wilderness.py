#! /usr/bin/env python
# -*- coding:utf-8 -*-
from db import Base

from sqlalchemy import Column, Integer, String
from sqlalchemy import event


class Wilderness(Base):
    __tablename__ = 'wilderness'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    chance = Column(Integer)

    def __repr__(self):
        return "<Wilderness#{}\t'{}':\t{}%>".format(self.id, self.description, self.chance)