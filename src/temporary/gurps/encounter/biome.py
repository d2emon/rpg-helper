#! /usr/bin/env python
# -*- coding:utf-8 -*-
from db import Base

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Biome(Base):
    __tablename__ = 'biome'
    id = Column(Integer, primary_key=True)
    wilderness_id = Column(Integer, ForeignKey('wilderness.id'))
    encounter_id = Column(Integer, ForeignKey('encounter_table.id'))
    wilderness = relationship("Wilderness")
    encounter_table = relationship("Table")
    description = Column(String)

    def __repr__(self):
        return "<Encounter#{}\t'{}'>".format(self.roll, self.description)