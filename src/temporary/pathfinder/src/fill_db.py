#! /usr/bin/env python
# -*- coding:utf-8 -*-
# from models.race import Race
from db import db_session


def main():
    import pathfinder.race
    human = pathfinder.race.raceHuman()
    # human.name = "Человек"
    # human.custom_ability = 2
    # human.bonus_feat = 1
    # human.bonus_skill = 1
    db_session.add(human)

    db_session.commit()


if __name__ == "__main__":
    main()
