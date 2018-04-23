#! /usr/bin/env python
# -*- coding:utf-8 -*-


def main(id=0, options=dict()):  # pragma: no cover
    """
    Main helper function
    """
    import logging
    logging.info("Starting helper")

    action = options.get("action", None)
    args = options.get("args", [])

    from gui.menu import showMenu

    from actions import runAction
    from actions import runById
    from actions.data import ACTIONS
    if action is not None:
        return runAction(action, *args)

    while True:
        showMenu(items=ACTIONS, func=runById)
    return True


if __name__ == "__main__":  # pragma: no cover
    import sys
    import getopt
    import gui
    import gui.commandline

    options = gui.commandline.parseArgs(sys.argv[1:], action=True)

    run_code = main(options=options)
    if run_code:
        sys.exit(0)
    else:
        gui.helpMessage()
