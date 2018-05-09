import random

worlds = [
  {'title': "Alternity", 'img': "alternity.gif"},
  {'title': "Birthright", 'img': "birthright.gif"},
  {'title': "Blackmoor", 'img': "blackmoor.jpg"},
  {'title': "Council of Wyrms", 'img': "council-of-wyrms.jpg"},
  {'title': "Creature Crucible", 'img': "creature-crucible.gif"},
  {'title': "Dangerous Fantasy 2", 'img': "df2.gif"},
  {'title': "Dark Sun", 'img': "darksun.gif"},
  {'title': "Dragon Fist", 'img': "dragon-fist.jpg"},
  {'title': "DragonLance", 'img': "dragonlance.gif"},
  {'title': "Eberron", 'img': "eberron.gif"},
  {'title': "Forgotten Realms", 'img': "forgotten-realms.gif"},
  {'title': "Ghostwalk", 'img': "ghostwalk.jpg"},
  {'title': "Greyhawk", 'img': "greyhawk.gif"},
  {'title': "Jakandor", 'img': "jakandor.jpg"},
  {'title': "Kingdoms of Kalamar", 'img': "kingdoms-of-kalamar.gif"},
  {'title': "Lankhmar", 'img': "lankhmar.gif"},
  {'title': "Mahasarpa", 'img': "mahasarpa.jpg"},
  {'title': "Mortal Kombat", 'img': "mortal-kombat.jpg"},
  {'title': "Mystara", 'img': "mystara.gif"},
  {'title': "Nentir Vale", 'img': "nentir-vale.jpg"},
  {'title': "Odyssey", 'img': "odyssey.gif"},
  {'title': "Oriental Adventures", 'img': "oriental-adventures.gif"},
  {'title': "Pelinore", 'img': "pelinore.jpg"},
  {'title': "Planescape", 'img': "planescape.jpg"},
  {'title': "Ravenloft", 'img': "ravenloft.gif"},
  {'title': "SCP Foundation"},
  {'title': "Spelljammer", 'img': "spelljammer.gif"},
  {'title': "S.T.A.L.K.E.R", 'img': "stalker.jpg"},
  {'title': "Thunder Rift", 'img': "thunder-rift.jpg"},
  {'title': "Warcraft", 'img': "warcraft.gif"},
  {'title': "Warhammer 40000"},
  {'title': "Wilderlands of High Fantasy", 'img': "wilderlands-of-high-fantasy.jpg"},
  {'title': "Авенхейм", 'img': "avenheim.jpg"},
  {'title': "Алиса Селезнева", 'img': "alice.png"},
  {'title': "Амбер", 'img': "amber.jpg"},
  {'title': "Арда", 'img': "tolkien.jpg"},
  {'title': "Белория", 'img': "beloria.jpg"},
  {'title': "Вестерос"},
  {'title': "Вечный Воитель", 'img': "eternal-warrior.jpg"},
  {'title': "Волшебная Страна", 'img': "emerald.jpg"},
  {'title': "Геройский Мир", 'img': "homm.jpg"},
  {'title': "Дино"},
  {'title': "Дюна"},
  {'title': "Конан", 'img': "conan.gif"},
  {'title': "Король и Шут", 'img': "kish.jpg"},
  {'title': "Крон", 'img': "chronos.jpg"},
  {'title': "Мир номер три", 'img': "tretiy-mir.jpg"},
  {'title': "Мир Полудня", 'img': "midday.jpg"},
  {'title': "Москва будущего", 'img': "moscow.jpg"},
  {'title': "Путеводитель по коридорам Ада", 'img': "hell.jpg"},
  {'title': "Спектр", 'img': "spectre.jpg"},
]

class World:
    images = [
        # "/static/images/world/0-house.jpg",
        # "/static/images/world/0-road.jpg",
        # "/static/images/world/0-plane.jpg",
        # "/static/images/world/0-sunshine.jpg",
        "https://lorempixel.com/400/300/",
    ]

    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.img = kwargs.get('img')
        self.subtitle = "1,000 miles of wonder"

    def full_img(self, path="/static/images/world"):
        if self.img is not None:
            return "{}/{}".format(path, self.img)
        else:
            return "{}?{}".format(random.choice(self.images), random.random())

    def as_dict(self, path="/static/images/world"):
        return {
            'title': self.title,
            'subtitle': self.subtitle,
            'img': self.full_img(path),
        }


def list_worlds():
    return [World(id=id, **world) for id, world  in enumerate(worlds)]
