from generator import ListGenerator


from .fixtures import environments, maps, atmospheres, suns


class Sun():
    def __init__(self, sun_type=None):
        self.sun_type = sun_type
        self.planets = []


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


class PlanetAtmosphere():
    def __init__(self, title, exist=True):
        self.title = title
        self.exist = exist
        
    def __repr__(self):
        return self.title


class PlanetGenerator():
    margin = 5.4
    atmospheres = [PlanetAtmosphere(a[0], a[1]) for a in atmospheres]
    environment = environments
    map = maps
    
    class PlanetType():
        earth = False
        max_moons = 60
        
        def __init__(self, image_id=1):
            self.image = image_id
        
        def __repr__(self):
            return self.image
    
    class EarthPlanet(PlanetType):
        earth = True
        max_moons = 5
        
        def __repr__(self):
            if self.image < 10:
                image = "0" + str(self.image)
            else:
                image = str(self.image)
            return "earthPlanet%s" % (image)
    
    class LayerPlanet(PlanetType):
        def __repr__(self):
            return "layerPlanet%s" % (self.image)
    
    class TerPlanet(PlanetType):
        def __repr__(self):
            return "terplanet%s" % (self.image)
    
    class MoonPlanet(PlanetType):
        def __repr__(self):
            return "moonPlanet%s" % (self.image)
    
    class GasPlanet(PlanetType):
        def __repr__(self):
            return "gasPlanet%s" % (self.image)

    @classmethod
    def generate(cls, near=False, earth=False):
        import random
        earthPlanets = [cls.EarthPlanet(i + 1) for i in range(40)]
        layerPlanets = [cls.LayerPlanet(i + 1) for i in range(40)]
        terplanets = [cls.TerPlanet(i + 1) for i in range(40)]
        moonPlanets = [cls.MoonPlanet(i + 1) for i in range(40)]
        gasPlanets = [cls.GasPlanet(i + 1) for i in range(40)]

        noEarthPlanets = (layerPlanets * 2) + terplanets + moonPlanets + gasPlanets
        combPlanets = earthPlanets + noEarthPlanets

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


class StarGenerator(ListGenerator):
    generated_class = Sun
    suns = suns

    @classmethod
    def generate(cls, planets=0, blue_sun=False, only_blue=False):
        generated = cls.generated()
        return cls.fill_generated(generated, planets=planets, blue_sun=blue_sun, only_blue=only_blue)
        
    @classmethod
    def fill_generated(cls, generated, planets=0, blue_sun=False, only_blue=False):
        import random
        suns = cls.suns
        if not blue_sun:
            suns = suns[:30]
        if only_blue:
            suns = suns[30:]

        sun_type = cls.generate_value(suns)                
        generated.sun_type = sun_type[0]
        if sun_type[1]:
            generated.sun_type += ".blue"

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