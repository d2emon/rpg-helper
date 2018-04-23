import pc


class Default(pc.PlayerCharacter):
    def __init__(self):
        pc.PlayerCharacter.__init__(self, "Default")

        self.setST(10)
        self.setDX(10)
        self.setIQ(10)
        self.setHT(10)


class Monk(pc.PlayerCharacter):
    def __init__(self):
        pc.PlayerCharacter.__init__(self, "Winnfred O'Poughann")

        self.setST(12)
        self.setDX(8)
        self.setIQ(12)
        self.setHT(10)
