#! /usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import Column, Integer, String, Date, UnicodeText, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from models import Base


class GameSystem(Base):
    __tablename__ = 'game_system'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    version = Column(String(16))
    website = Column(String(255))
    campaigns = relationship("Campaign")

    def __repr__(self):
        return "{} ({})".format(self.name, self.version)


class Campaign(Base):
    __tablename__ = 'campaign'
    id = Column(Integer, primary_key=True)
    gs_id = Column(Integer, ForeignKey('game_system.id'))
    title = Column(String(32))
    sessions = relationship("GameSession")
    characters = relationship("GameCharacter")

    def __repr__(self):
        return self.title


class GameSession(Base):
    __tablename__ = 'game_session'
    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, ForeignKey('campaign.id'))
    real_date = Column(Date, server_default=func.now())
    title = Column(String(32))
    description = Column(UnicodeText())

    def __repr__(self):
        if self.title:
            return self.title
        return str(self.real_date)


class GameCharacter(Base):
    __tablename__ = 'game_character'
    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, ForeignKey('campaign.id'))

    def __repr__(self):
        title = "Char {}".format(self.id)
        return title
