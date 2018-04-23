#! /usr/bin/env python
# -*- coding:utf-8 -*-


import unittest
import getopt

import generate
import pathfinder.character.rooster


class TestGenerateFunctions(unittest.TestCase):
    def setUp(self):
        self.rooster = pathfinder.character.rooster.Rooster()
        self.rooster.add(count=5)

    def testWrongArgs(self):
        '''
        Ensure that help text is shown on wrong arguments
        '''
        self.assertRaises(getopt.GetoptError, generate.parseArgs, ["-a"])

    def testHelpOption(self):
        '''
        Ensure that help text is shown on -h
        '''
        self.assertRaises(getopt.GetoptError, generate.parseArgs, ["-h"])

    def testParse(self):
        '''
        Ensure that main function runs succesfully
        '''
        import ruleset

        logfile = "pathfinder.log"
        logformat = '%(asctime)s: [%(levelname)s]:\t%(message)s'

        c = 5
        filename = "test.yml"
        method = "heroic"
        args = ["-d", "-l", logfile, "-c", c, "-f", filename, "--roll", method, "--logformat", logformat]
        parsed = generate.parseArgs(args)

        self.assertEqual(int(parsed.get("count", 0)), c)

        rules = parsed.get("rules", None)
        self.assertIsInstance(rules, ruleset.Ruleset)
        self.assertIs(rules.rollMethod, ruleset.ruleset.roll.HEROIC)

    def testPickRace(self):
        chars = generate.pickRace(self.rooster.chars)
        self.assertEqual(len(chars), len(self.rooster.chars))

    def testPickClass(self):
        chars = generate.pickClass(self.rooster.chars)
        self.assertEqual(len(chars), len(self.rooster.chars))

    def testPickSkills(self):
        chars = generate.pickSkills(self.rooster.chars)
        self.assertEqual(len(chars), len(self.rooster.chars))

    def testBuyEquipment(self):
        chars = generate.buyEquipment(self.rooster.chars)
        self.assertEqual(len(chars), len(self.rooster.chars))

    def testFinishDetails(self):
        chars = generate.finishDetails(self.rooster.chars)
        self.assertEqual(len(chars), len(self.rooster.chars))

    def testHelpMessage(self):
        '''
        Ensure program exits after help message
        '''
        self.assertRaises(SystemExit, generate.helpMessage)

    def testCreateChars(self):
        chars = generate.createChars(self.rooster)
        self.assertEqual(chars, self.rooster)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
