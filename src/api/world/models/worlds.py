import random

from world.default import worlds

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
