#! /usr/bin/env python
# -*- coding:utf-8 -*-


import random


class MCDict:
    def __init__(self, chainlen=2, filename=None):
        self.d = {}
        if chainlen > 10 or chainlen < 1:
            print("Chain length must be between 1 and 10, inclusive")
            # sys.exit(0)

        self.chainlen = chainlen
        if filename is not None:
            self.loadLines(filename)

    def __getitem__(self, key):
        if key in self.d:
            return self.d[key]
        else:
            raise KeyError(key)

    def add_key(self, prefix, suffix):
        if prefix in self.d:
            self.d[prefix].append(suffix)
        else:
            self.d[prefix] = [suffix]

    def add_element(self, element):
        s = " " * self.chainlen + element
        for n in range(0, len(element)):
            self.add_key(s[n:n+self.chainlen], s[n+self.chainlen])
        self.add_key(s[len(element):len(element)+self.chainlen], "\n")

    def get_suffix(self, prefix):
        l = self[prefix]
        return random.choice(l)

    def loadLines(self, filename):
        from models import LinesFile
        lines = LinesFile(filename)
        for line in lines:
            self.add_element(line.data.strip())


class MCName:
    """
    A name from a Markov chain
    """
    max_length = 15  # 9

    def __init__(self, chainlen=2):
        """
        Building the dictionary
        """
        self.mcd = MCDict(chainlen, "db/names/names.txt")

    def New(self):
        """
        New name from the Markov chain
        """
        prefix = " " * self.mcd.chainlen
        name = ""
        suffix = ""
        while True:
            suffix = self.mcd.get_suffix(prefix)
            if suffix == "\n" or len(name) > self.max_length:
                break
            else:
                name = name + suffix
                prefix = prefix[1:] + suffix
        return name.capitalize()


class MCRussianName(MCName):
    """
    A name from a Markov chain
    """
    max_length = 15  # 9

    def __init__(self, chainlen=2):
        """
        Building the dictionary
        """
        self.mcd = MCDict(chainlen, "db/names/russian/names1-m.txt")
        self.mcd2 = MCDict(chainlen, "db/names/russian/names2-m.txt")
        self.mcd3 = MCDict(chainlen, "db/names/russian/names3-m.txt")

    def NewPart(self, mcd):
        """
        New name from the Markov chain
        """
        prefix = " " * mcd.chainlen
        name = ""
        suffix = ""
        while True:
            suffix = mcd.get_suffix(prefix)
            if suffix == "\n" or len(name) > self.max_length:
                break
            else:
                name = name + suffix
                prefix = prefix[1:] + suffix
        return name.capitalize()

    def NewFull(self):
        return "{} {} {}".format(
            self.NewPart(self.mcd),
            self.NewPart(self.mcd2),
            self.NewPart(self.mcd3),
        )
