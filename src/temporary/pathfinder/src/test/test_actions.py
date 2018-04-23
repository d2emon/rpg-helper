#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
Testing actions
"""

import unittest
import mock
import random
import actions
import actions.editions


class TestActions(unittest.TestCase):
    def testNoAction(self):
        '''
        Ensure that returns False on no action
        '''
        self.assertFalse(actions.runAction(None))

    def testBadAction(self):
        '''
        Ensure that returns False on bad action
        '''
        self.assertFalse(actions.runAction("bad_action"))

    def testAdventureAction(self):
        '''
        Ensure that returns False on adventure
        '''
        with mock.patch('builtins.input', return_value='0'):
            with self.assertRaises(SystemExit):
                self.assertFalse(actions.runAction('adventure'), "Wrong adventure action")

    def testEquipmentAction(self):
        '''
        Ensure that returns False on equipment
        '''
        with mock.patch('builtins.input', return_value='0'):
            with self.assertRaises(SystemExit):
                self.assertFalse(actions.runAction('equipment'), "Wrong equipment action")

    def testEncounterAction(self):
        '''
        Ensure that returns False on encounter
        '''
        with mock.patch('builtins.input', return_value='0'):
            with self.assertRaises(SystemExit):
                self.assertFalse(actions.runAction('encounter'), "Wrong encounter action")

    def testGenerateAction(self):
        '''
        Ensure that returns False on generate
        '''
        with mock.patch('builtins.input', return_value='0'):
            with self.assertRaises(SystemExit):
                self.assertFalse(actions.runAction('generate'), "Wrong generate action")

    def testByIdNegative(self):
        '''
        Ensure that returns False on negative action id
        '''
        with mock.patch('builtins.input', return_value='0'):
            with self.assertRaises(SystemExit):
                actions.runById(-1)

    def testByIdPositive(self):
        '''
        Ensure that returns False on positive action id
        '''
        import actions.data
        action_id = random.randrange(1, len(actions.data.ACTIONS))
        self.assertFalse(actions.runById(action_id))

    def testByIdBig(self):
        '''
        Ensure that returns False on big action id
        '''
        with self.assertRaises(IndexError):
            actions.runById(256)

    def testPathfinder(self):
        '''
        Ensure that returns False using Pathfinder
        '''
        with mock.patch('builtins.input', return_value='0'):
            with self.assertRaises(SystemExit):
                self.assertFalse(actions.editions.pathfinder(random.randint(-255, 255)))

    def testDnd(self):
        '''
        Ensure that returns False using DnD
        '''
        with mock.patch('builtins.input', return_value='0'):
            with self.assertRaises(SystemExit):
                self.assertFalse(actions.editions.dnd(random.randint(-255, 255)))

    def testCyclo(self):
        '''
        Ensure that returns False using Cyclo
        '''
        with mock.patch('builtins.input', return_value='0'):
            with self.assertRaises(SystemExit):
                self.assertFalse(actions.editions.cyclo(random.randint(-255, 255)))

    def testBookSelection(self):
        '''
        Ensure that returns False on selecting book
        '''
        with self.assertRaises(IndexError):
            actions.editions.selectBook(random.randint(-255, 255))

    def testMenu(self):
        '''
        Ensure that returns False on entering menu
        '''
        with mock.patch('builtins.input', return_value='0'):
            with self.assertRaises(SystemExit):
                self.assertFalse(actions.editions.menu(random.randint(-255, 255)))


def main():
    unittest.main()


if __name__ == "__main__":
    main()
