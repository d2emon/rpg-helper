from generator import ListGenerator


from .fixtures import atmospheres, environments, maps, suns, non_earthPlanets, allPlanets
from .planet import PlanetGenerator


class Sun():
    def __init__(self, sun_type=None):
        self.sun_type = sun_type
        self.planets = []



class StarGenerator(ListGenerator):
    generated_class = Sun
    suns = suns[30:]
    blue_suns = suns[:30]

    @classmethod
    def generate(cls, planets=0, blue_sun=False, only_blue=False):
        generated = cls.generated()
        return cls.fill_generated(generated, planets=planets, blue_sun=blue_sun, only_blue=only_blue)
        
    @classmethod
    def fill_generated(cls, generated, planets=0, blue_sun=False, only_blue=False):
        import random
        suns = cls.suns
        if blue_sun:
            suns += cls.blue_suns
        if only_blue:
            suns = cls.blue_suns

        generated.sun_type = cls.generate_value(suns)

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