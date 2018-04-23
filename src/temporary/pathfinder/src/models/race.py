#! /usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import Column, Integer, String, UnicodeText
from models import Base


SIZE_SMALL = -1
SIZE_MEDIUM = 0

SIZE_DESC = {
    SIZE_SMALL: "Маленький",
    SIZE_MEDIUM: "Средний",
}


SPEED_MEDIUM = 30


class Race(Base):
    __tablename__ = 'race'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    #    self.blood = UNKNOWN_ID
    #    self.abilities = dict()
    #    self.randAbility = []
    custom_ability = Column(Integer, default=0)
    bonus_feat = Column(Integer, default=0)
    bonus_skill = Column(Integer, default=0)
    size_bonus = Column(Integer, default=SIZE_MEDIUM)
    speed = Column(Integer, default=SPEED_MEDIUM)
    #    self.lowlight = 1
    #    self.darkvision = 0
    #    self.favouredClasses = 1
    #    self.feats = []
    #    self.weapons = []
    #    self.weaponGroups = []
    #    self.languages = ["common"]
    #    self.additionalLanguages = []
    #    self.anyLanguage = False
    description = Column(UnicodeText())

    def __repr__(self):
        return self.name

    def size(self):
        return SIZE_DESC.get(self.size_bonus)

    def languages(self):
        return ["Всеобщий", ]
