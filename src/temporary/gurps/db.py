#! /usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


engine = None
dbAddr = "sqlite:///db/gurps.db"

def connect(echo=False):
    global engine, dbAddr

    if engine is None:
        from sqlalchemy import create_engine
        engine = create_engine("sqlite:///db/gurps.db", echo=echo)

    global Base
    Base.metadata.create_all(engine, checkfirst=True)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)

    return engine, Session()
