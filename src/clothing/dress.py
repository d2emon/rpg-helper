from fixtures.clothing import dress, belt, sleeves

import random


class DressPart:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return self.title


class DressType(DressPart):
    pass


class Neckline(DressPart):
    pass


class Reveal(DressPart):
    pass


class Fabric(DressPart):
    pass


class DressStomach(DressPart):
    pass


class DressOpen(DressPart):
    pass


class DressFront(DressPart):
    pass


class DressBack(DressPart):
    pass


class DressEnd(DressPart):
    pass


class DressOutline(DressPart):
    pass


class BeltType(DressPart):
    pass


class BeltStyle(DressPart):
    pass


class BeltPosition(DressPart):
    pass


class SleevesLength(DressPart):
    pass


class SleevesWidth(DressPart):
    pass


class SleevesDivide(DressPart):
    pass


class SleevesBelt(DressPart):
    pass


class SleevesBand(DressPart):
    pass


class Belt:
    def __init__(self, **kwargs):
        self.beltType = kwargs.get('beltType')
        self.beltStyle = kwargs.get('beltStyle')
        self.position = kwargs.get('position')

    def __repr__(self):
        return self.title

    @classmethod
    def generate(cls):
        beltTypes = [BeltType(i) for i in belt.beltTypes]
        beltStyles = [BeltStyle(i) for i in belt.beltStyles]
        positions = [BeltPosition(i) for i in belt.positions]

        return cls(
            beltType=random.choice(beltTypes),
            beltStyle=random.choice(beltStyles),
            position=random.choice(positions),
        )

    @property
    def title(self):
        return self.beltStyle.title

    @property
    def description(self):
        return "{} {}, который она носит {} на талии.'".format(
            self.beltType.title,
            self.beltStyle.title,
            self.position.title,
        )


class Dress:
    def __init__(self, **kwargs):
        self.dressType = kwargs.get('dressType')
        self.neckline = kwargs.get('neckline')
        self.reveal = kwargs.get('reveal')
        self.fabric = kwargs.get('fabric')
        self.stomach = kwargs.get('stomach')
        self.open = kwargs.get('open')
        self.front = kwargs.get('front')
        self.back = kwargs.get('back')
        self.end = kwargs.get('end')
        self.sleevesLength = kwargs.get('sleevesLength')
        self.sleevesWidth = kwargs.get('sleevesWidth')
        self.sleevesDivide = kwargs.get('sleevesDivide')
        self.sleevesChange = kwargs.get('sleevesChange')
        self.sleevesBelt = kwargs.get('sleevesBelt')
        self.sleevesBand = kwargs.get('sleevesBand')
        self.outline = kwargs.get('outline')

    def __repr__(self):
        return self.title

    @classmethod
    def generate(cls):
        dressTypes = [DressType(i) for i in dress.description]
        necklines = [Neckline(i) for i in dress.necklines]
        reveals = [Reveal(i) for i in dress.reveals]
        fabrics = [Fabric(i) for i in dress.fabrics]
        stomachs = [DressStomach(i) for i in dress.stomachs]
        opens = [DressOpen(i) for i in dress.opens]
        fronts = [DressFront(i) for i in dress.fronts]
        backs = [DressBack(i) for i in dress.backs]
        ends = [DressEnd(i) for i in dress.ends]
        sleevesLengths = [SleevesLength(i) for i in sleeves.lengths]
        sleevesWidths = [SleevesWidth(i) for i in sleeves.widths]
        sleevesDivides = [SleevesDivide(i) for i in sleeves.divides]
        sleevesBelts = [SleevesBelt(i) for i in belt.beltTypes]
        sleevesBands = [SleevesBand(i) for i in sleeves.bands]
        outlines = [DressOutline(i) for i in dress.outlines]

        d = cls(
            dressType=random.choice(dressTypes),
            neckline=random.choice(necklines),
            reveal=random.choice(reveals),
            fabric=random.choice(fabrics),
            stomach=random.choice(stomachs),
            open=random.choice(opens),
            front=random.choice(fronts),
            back=random.choice(backs),
            end=random.choice(ends),
            sleevesLength=random.choice(sleevesLengths),
            sleevesWidth=random.choice(sleevesWidths),
            sleevesDivide=random.choice(sleevesDivides),
            sleevesChange=random.choice([True, False]),
            sleevesBelt=random.choice(sleevesBelts),
            sleevesBand=random.choice(sleevesBands),
            outline=random.choice(outlines),
        )
        ud = UnderDress(dressType=random.choice(dressTypes))
        while ud.dressType == d.dressType:
            ud.dressType = random.choice(dressTypes)
        b = Belt.generate()
        return d, ud, b

    @property
    def title(self):
        return  "{} платье".format(self.dressType)

    def describe(self, underDress, belt):
        sleevesChange = ''
        if self.sleevesChange:
            sleevesChange = "меняют цвет и "
        # rnd4 = rnd4[0].toUpperCase() + rnd4.substring(1)

        description = "Она одета в {} с {}, который {} открывает {}. ".format(
            self.title,
            self.neckline,
            self.reveal,
            underDress.title,
        )
        description += "{} {} её платья покрывает живот, где непрерывный поток платья прерывается {}.'".format(
            self.fabric,
            self.stomach,
            belt.description,
        )
        description += "\n"
        description += "Под {} платье {} нижнее платье. ".format(
            belt.title,
            self.open,
        )
        description += "Передний край верхнего платья {}, а задний образует {} шлейф и оканчивается {}.".format(
            self.front,
            self.back,
            self.end,
        )
        description += "\n"
        description += "Её рукава {} и {}, {} они {} отделаны {}, {} пояском из того же материала, что и отделка {} платья.".format(
            self.sleevesLength,
            self.sleevesWidth,
            self.sleevesDivide,
            sleevesChange,
            self.sleevesBelt,
            self.sleevesBand,
            self.outline,
        )
        return description


class UnderDress(Dress):
    @property
    def title(self):
        return  "{} нижнее платье".format(self.dressType)


def generateDress():
    d, ud, b = Dress.generate()
    return {
        'dress': {
            'title': d.title,
            'description': d.describe(ud, b),
        },
        'underdress': ud,
        'belt': b,
    }
