#! /usr/bin/env python
# -*- coding:utf-8 -*-


from actions.data import ACTIONS
from actions.data import CMDS


def runAction(action, *args):
    if action is None:
        return False

    import logging
    logging.debug("Running %s", action)

    cmd = CMDS.get(action, None)
    if cmd is None:
        return False

    return cmd(0, *args)


def runById(actionId):
    action = ACTIONS[actionId].get("action", None)
    if action is None:
        return False  # actionId
    return action(actionId)
