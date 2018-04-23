#! /usr/bin/env python
# -*- coding:utf-8 -*-
from db import Base

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class EncounterPoint(Base):
    __tablename__ = 'encounter_point'
    id = Column(Integer, primary_key=True)
    encounter_table = relationship("Table")
    roll = Column(Integer)
    description = Column(String)

    def __repr__(self):
        return "<Encounter#{}\t'{}'>".format(self.roll, self.description)
    
        
class Table(Base):
    __tablename__ = 'encounter_table'
    id = Column(Integer, primary_key=True)
    description = Column(String)

    def __repr__(self):
        return "<Table#{}\t'{}'>".format(self.id, self.description)