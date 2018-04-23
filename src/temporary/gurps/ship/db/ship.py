shipSizeDB = [
    {
        "title": "Small sloop",
        "tonnage": [50, 100],
        "length": [15, 20],
        "beam": [4, 6],
        "masts": 1,
        "draft": [7, 9],
    },
    {
        "title": "Large sloop",
        "tonnage": [80, 200],
        "length": [20, 30],
        "beam": [5, 8],
        "masts": 1,
        "draft": [8, 11],
    },
    {
        "title": "Small brig",
        "tonnage": [150, 400],
        "length": [25, 30],
        "beam": [8, 11],
        "masts": 2,
        "draft": [12, 20],
    },
    {
        "title": "Large brig",
        "tonnage": [500, 1500],
        "length": [30, 50],
        "beam": [9, 20],
        "masts": 2,
        "draft": [12, 20],
    },
    {
        "title": "Small ship",
        "tonnage": [600, 900],
        "length": [25, 40],
        "beam": [7, 12],
        "masts": 3,
        "draft": [16, 25],
    },
    {
        "title": "Large ship",
        "tonnage": [1000, 2000],
        "length": [40, 60],
        "beam": [15, 20],
        "masts": 3,
        "draft": [16, 25],
    },
]


shipCostDB = [
    {
        "title": "Small Sloop",
        "id": [0, ],
        "speed": [12, 16],
        "maneuver": [1, 3],
        "firepower": [0, 50],
        "cost": 40000,
    },
    {
        "title": "Large Sloop",
        "id": [1, ],
        "speed": [10, 14],
        "maneuver": [2, 4],
        "firepower": [80, 100],
        "cost": 75000,
    },
    {
        "title": "Small Merchant Brig",
        "id": [2, 3],
        "speed": [8, 10],
        "maneuver": [2, 5],
        "firepower": [35, 75],
        "cost": 75000,
    },
    {
        "title": "Small War Brig",
        "id": [2, 3],
        "speed": [9, 12],
        "maneuver": [3, 5],
        "firepower": [170, 300],
        "cost": 200000,
    },
    {
        "title": "Merchant Ship",
        "id": [4, 5],
        "speed": [6, 9],
        "maneuver": [4, 6],
        "firepower": [45, 135],
        "cost": 200000,
    },
    {
        "title": "Large Warship",
        "id": [4, 5],
        "speed": [7, 10],
        "maneuver": [4, 6],
        "firepower": [45, 135],
        "cost": 800000,
    },
]


class ShipTemplate:
    def __init__(self, id=0):
        template = shipCostDB[id]
        sizeTemplate = shipSizeDB[id]
        self.title = "{}({})".format(template.get("title"), sizeTemplate.get("title"))
        self.speed = template.get("speed", [12, 16])
        self.maneuver = template.get("maneuver", [1, 3])
        self.firepower = template.get("firepower", [0, 50])
        self.cost = template.get("cost", 40000)
        self.tonnage = sizeTemplate.get("tonnage", [50, 100])
        self.length = sizeTemplate.get("length", [15, 20])
        self.beam = sizeTemplate.get("beam", [4, 6])
        self.masts = sizeTemplate.get("masts", 1)
        self.draft = sizeTemplate.get("draft", [7, 9])


def getShipData(id):
    template = ShipTemplate(id)

    import random
    ship = {
        "title": template.title,
        "tonnage": random.randrange(*template.tonnage),
        "length": random.randrange(*template.length),
        "beam": random.randrange(*template.beam),
        "masts": template.masts,
        "draft": random.randrange(*template.draft),
        "speed": template.speed,
        "maneuver": -random.randrange(*template.maneuver),
        "firepower": random.randrange(*template.firepower),
        "cost": template.cost,
    }
    return ship


if __name__ == "__main__":
    import random
    id = random.randrange(0, 6)
    ship = getShipData(id)
    print(ship)
