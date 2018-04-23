import pc


class TestCharacter(pc.PlayerCharacter):
    def __init__(self):
        pc.PlayerCharacter.__init__(self, "Winnfred O'Poughann")

        self.setST(12)
        self.attributes["DX"].value = 8
        self.attributes["IQ"].value = 12
        self.attributes["HT"].value = 10
