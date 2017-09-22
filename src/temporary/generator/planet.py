from .fixtures import atmospheres, environments, maps, non_earthPlanets, allPlanets


class Planet():
    """
    <div class=\"planClose\" style=\"background-image: url('../images/planets/" + planet + ".png');\"></div>\
    <div class=\"planDetails\">\
        <textarea class=\"env\">Environment: " + environment[rnEnv] + "</textarea>\
        <textarea class=\"atmos\">Atmosphere: " + atmospheres[rnAtmos] + "</textarea>\
        <textarea class=\"map\">Surface map available: " + map[rnMap] + "</textarea>\
        <textarea class=\"day\">Day duration: " + rnDay + " hours</textarea>\
        <textarea class=\"grav\">Gravity: " + rnGrav + " (compared to Earth)</textarea>\
        <textarea class=\"orbit\">Orbit duration: " + rnOrbit + " Earth years</textarea>\
        <textarea class=\"moons\">Number of moons: " + rnMoons + "</textarea>\
        <textarea class=\"tilt\">Axial tilt: " + rnTilt + "&#176;</textarea>\
    </div>");
    """
    def __init__(self, **kwargs):
        self.planet_type = kwargs.get('planet_type')
        self.environment = kwargs.get('environment')
        self.atmosphere = kwargs.get('atmosphere')
        self.surface_map = kwargs.get('surface_map')
        self.hours = kwargs.get('hours')
        self.gravity = kwargs.get('gravity')
        self.days = kwargs.get('days')
        self.moons = kwargs.get('moons')
        self.tilt = kwargs.get('tilt')

        self.margin_left = kwargs.get('margin_left')
        self.width = kwargs.get('width')


class PlanetGenerator():
    margin = 5.4
    atmospheres = atmospheres
    environment = environments
    map = maps

    @classmethod
    def generate(cls, near=False, earth=False):
        import random
        noEarthPlanets = non_earthPlanets
        combPlanets = allPlanets

        rnMargin = (random.random() * cls.margin - 0.9 + 1) + 0.9
        # if i < 6:
        if near:
            if not earth:
                planet_type = random.choice(combPlanets)
                # combPlanets.splice(ranPlanet, 1);
                if planet_type.earth:
                    earth = True
            else:
                planet_type = random.choice(noEarthPlanets)
                # combPlanets.splice(ranPlanet, 1);
        else:
            planet_type = random.choice(noEarthPlanets)
            
        if planet_type.earth:
            dayType = 1
            orbitType = 1
            atmospheres=cls.atmospheres[1:]
        else:
            dayType = random.randrange(2)
            orbitType = random.randrange(2)
            atmospheres=cls.atmospheres

        if dayType == 1:
            hours = random.randrange(43) + 8
        else:
            hours = random.randrange(4001) + 2000

        if orbitType == 1:
            days = ((random.random() * 2.8) + 0.2)
        else:
            days = ((random.random() * 191) + 10)
            
        return Planet(
            planet_type=planet_type,
            margin_left=rnMargin,
            width=random.randrange(51) + 20,
            environment=random.choice(cls.environment),
            surface_map=random.choice(cls.map),
            atmosphere=random.choice(atmospheres),
            hours=hours,
            days=days,
            gravity=((random.random() * 4.8) + 0.2),
            moons=random.randint(1, planet_type.max_moons),
            tilt=random.random() * 180
        )