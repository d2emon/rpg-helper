from app import db
from generator.space.galaxy import GalaxyGenerator


class Galaxy(db.Model):
    """
    Create a Galaxy table
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False, info={'label': "Title"})
    description = db.Column(db.UnicodeText(), info={'label': "Description"})
    world_id = db.Column(db.Integer, db.ForeignKey('world.id'))

    world = db.relationship('World', backref='galaxies')
    
    @classmethod
    def generator(cls):
        from generator.space.fixtures import galaxy_names
        gn = GalaxyName.query.all()
        gt = GalaxyType.query.all()
        gp = galaxy_names[1]
        gf = galaxy_names[2]

        g = GalaxyGenerator
        g.GalaxyGenerator1.galaxy_names = [gn, gp]
        g.GalaxyGenerator2.galaxy_names = [gp, gt]
        g.GalaxyGenerator3.galaxy_names = [gf, gt]
        return g

    @classmethod
    def generate(cls, **kwargs):
        title = kwargs.get('title')
        world_id = kwargs.get('world_id') 
        if not title:
            title = cls.generator().generate().title
        return cls(title=title, world_id=world_id)

    def __repr__(self):
        if self.title is None:
            return "<UNTITLED>"
        else:
            return self.title
        

class GeneratorData:
    """
    Basic class for generator data
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False, info={'label': "Title"})

    def __repr__(self):
        if self.title is None:
            return "<UNTITLED>"
        else:
            return self.title

class GalaxyName(GeneratorData, db.Model):
    """
    Create a GalaxyName table
    """
        

class GalaxyPlacement(GeneratorData, db.Model):
    """
    Create a GalaxyPlacement table
    """
        

class GalaxyForm(GeneratorData, db.Model):
    """
    Create a GalaxyForm table
    """
                

class GalaxyType(GeneratorData, db.Model):
    """
    Create a GalaxyType table
    """


class Sun():
    def __init__(self, sun_type=None):
        self.sun_type = sun_type
        self.planets = []
        # css__planetCont = None
        
    @property
    def image(self):
        return "../images/planets/%s.png" % (self.sun_type)


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
    atmospheres = [
        PlanetAtmosphere("None", False),
        PlanetAtmosphere("Thick"),
        PlanetAtmosphere("Thin"),
        PlanetAtmosphere("Unknown"),
        PlanetAtmosphere("Fairly thick"),
        PlanetAtmosphere("Fairly thin"),
        PlanetAtmosphere("Very thick"),
        PlanetAtmosphere("Very thin")
    ]
    environment = [
        "Hospitable",
        "Gentle",
        "Moderate",
        "Fairly gentle",
        "Fairly hospitable",
        "Unknown",
        "Quite hostile",
        "Hostile",
        "Very hostile",
        "Dangerous",
        "Very dangerous",
        "Deadly",
        "Unsafe",
        "Treacherous",
        "Unstable"
    ]
    map = ["Yes","No","Outdated version"]
    
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


class StarGenerator():
    suns = ["sun%d" % (i + 1) for i in range(30)] + ["blue_sun%d" % (i + 30) for i in range(10)]

    drag = "on"
    res = "on"
    ttl = 0
        
    def rndSolar(self, num_planets=0, blue_sun=False, only_blue=False):
        import random

        earth = False
        
        if num_planets > 0:
            nrPlanets = num_planets
        else:
            nrPlanets = random.randrange(7) + 4
            
        sun_type = random.choice(self.suns)
        if blue_sun:
            while self.suns.index(sun_type) > 29:
                sun_type = random.choice(self.suns)
        if only_blue:
            while self.suns.index(sun_type) < 30:
                sun_type = random.choice(self.suns)
                
        sun = Sun(sun_type)

        for i in range(nrPlanets):
            planet = PlanetGenerator.generate(i < 6, earth)
            # curPlanet = planet.slice(0, -2)
            if planet.planet_type.earth:
                earth = True
            sun.planets.append(planet)
        return sun

class Star(db.Model):
    """
    Create a Galaxy table
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False, info={'label': "Title"})
    galaxy_id = db.Column(db.Integer, db.ForeignKey('galaxy.id'))

    galaxy = db.relationship('Galaxy', backref='stars')

    @classmethod
    def generate(cls):
        g = StarGenerator()
        s = g.rndSolar(blue_sun=True)
        print(s.sun_type)
        for id, p in enumerate(s.planets):
            print(id + 1, p.planet_type)
            print(p.margin_left, p.width)
            print("\tEnvironment:\t\t%s" % (p.environment))
            print("\tAtmosphere:\t\t%s" % (str(p.atmosphere)))
            print("\tSurface map available:\t%s" % (p.surface_map))
            print("\tDay duration:\t\t%s hours" % (p.hours))
            print("\tGravity:\t\t%s (compared to Earth)" % (p.gravity))
            print("\tOrbit duration:\t\t%s Earth years" % (p.days))
            print("\tNumber of moons:\t%s" % (p.moons))
            print("\tAxial tilt:\t\t%s&#176;" % (p.tilt))
    
    def __repr__(self):
        if self.title is None:
            return "<UNTITLED>"
        else:
            return self.title
