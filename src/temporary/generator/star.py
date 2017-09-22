from generator import ListGenerator


from .fixtures import suns
from .planet import PlanetGenerator


class Sun():
    def __init__(self, sun_type=None):
        self.sun_type = sun_type
        self.planets = []


class StarGenerator(ListGenerator):
    generated_class = Sun
    sun_list = suns[:30]
    blue_sun_list = suns[30:]

    @classmethod
    def generate(cls, planets=0, blue_sun=False, only_blue=False):
        generated = cls.generated()
        return cls.fill_generated(generated, planets=planets, blue_sun=blue_sun, only_blue=only_blue)
        
    @classmethod
    def fill_generated(cls, generated, planets=0, blue_sun=False, only_blue=False):
        import random
        sun_list = cls.sun_list
        if blue_sun:
            sun_list += cls.blue_sun_list
        if only_blue:
            sun_list = cls.blue_sun_list

        generated.sun_type = cls.generate_value(sun_list)

        if not planets:
            planets = random.randrange(7) + 4

        earth = False
        for i in range(planets):
            planet = PlanetGenerator.generate(i < 6, earth)
            # curPlanet = planet.slice(0, -2)
            if planet.planet_type.earth:
                earth = True
            generated.planets.append(planet)
        return generated    