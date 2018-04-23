#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
Commandline parser
"""

import gui


def setupLog(options):
    """
    Setting up logger
    """
    import logging
    # logger = logging.getLogger()
    config = dict()

    # Default values
    filename = None
    logformat = "%(asctime)s: [%(levelname)s]:\t%(message)s"

    # Set log format
    logformat = options.get("--logformat", logformat)
    config['format'] = logformat
    formatter = logging.Formatter(logformat)

    # Debug mode
    if gui.DEBUG:
        config['level'] = logging.DEBUG
        filename = '../log/debug.log'

        gui.logger.setLevel(config['level'])

        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        gui.logger.addHandler(handler)

    # Set log file name
    filename = options.get("-l", filename)
    if filename is None:
        filename = options.get("--logfile")

    # Setting up handlers
    if filename is not None:
        config['filename'] = filename
        handler = logging.FileHandler(filename)
    else:
        handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    gui.logger.addHandler(handler)

    # print(config)
    logging.basicConfig(**config)
    return gui.logger


def parseArgs(argv, action=False):
    """
    Parsing argv for arguments
    """
    import getopt
    opts, args = getopt.getopt(argv, "hdl:c:r:f:", ["help", "debug", "logfile=", "count", "roll=", "file=", "logformat="])

    options = {opt: arg for opt, arg in opts}

    # Entering debug mode
    import os
    gui.DEBUG = os.environ.get('DEBUG', gui.DEBUG)
    if any(key in options.keys() for key in ("-d", "--debug")):
        gui.DEBUG = True

    setupLog(options)
    try:
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                raise getopt.GetoptError("")
            elif opt in ("-c", "--count"):
                options["count"] = int(arg)
            elif opt in ("-r", "--roll"):
                import pathfinder.ruleset
                methods = {
                    "standard": pathfinder.ruleset.roll.STANDARD,
                    "classic": pathfinder.ruleset.roll.CLASSIC,
                    "heroic": pathfinder.ruleset.roll.HEROIC,
                }
                options["rollMethod"] = methods[arg]
        if len(args) > 0:
            if action:
                options["action"] = args.pop(0)
            options["args"] = args
    except getopt.GetoptError:
        return gui.helpMessage()

    return options
