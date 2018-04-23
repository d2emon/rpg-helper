#! /usr/bin/env python
# -*- coding:utf-8 -*-


import gui


def showMenu(title="", items=[], func=None, args=dict()):
    """
    Showing menu
    """
    while True:
        print(title)
        for i, t in enumerate(items):
            if isinstance(t, dict):
                t = t.get("title", "Unknown")
            print("%d.\t%s" % (i + 1, t))
        print("-" * 80)
        print("0.\tExit")
        try:
            res = int(input("Enter your choice:\t")) - 1
            print("-" * 80)
            if res < 0:
                gui.bye()
            if func is not None:
                return func(res, **args)
            else:
                return res
        except (ValueError):
            print("Wrong choice!\n")
