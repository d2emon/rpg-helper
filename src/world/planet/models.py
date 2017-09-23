from flask import url_for
 
 
from app import db
from generator.space.star import StarGenerator
from generator.space.planet import PlanetGenerator1
from ..galaxy.models import GeneratorData
from ..star.models import Star
                

class PlanetType(GeneratorData, db.Model):
    """
    Create a PlanetType table
    """
                

class Environment(GeneratorData, db.Model):
    """
    Create a Environment table
    """
                

class Atmosphere(GeneratorData, db.Model):
    """
    Create a Atmosphere table
    """
                

class SurfaceMap(GeneratorData, db.Model):
    """
    Create a SurfaceMap table
    """


class Planet(db.Model):
    """
    Create a Planet table
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False, info={'label': "Title"})
    image = db.Column(db.String(32), nullable=True, info={'label': "Image"})
    size = db.Column(db.Float(2), default=1, info={'label': "Size"})
    from_sun = db.Column(db.Float(2), default=0, info={'label': "From sun"})
    day = db.Column(db.Float(2), default=24, info={'label': "Day duration"})
    year = db.Column(db.Float(2), default=365, info={'label': "Year duration"})
    gravity = db.Column(db.Float(2), default=1, info={'label': "Gravity"})
    moons = db.Column(db.Integer, default=1, info={'label': "Moons"})
    tilt = db.Column(db.Float(2), default=1, info={'label': "Axial tilt"})
    description = db.Column(db.UnicodeText(), info={'label': "Description"})
    star_id = db.Column(db.Integer, db.ForeignKey('star.id'), nullable=True)
    planet_type_id = db.Column(db.Integer, db.ForeignKey('planet_type.id'), nullable=True)
    environment_id = db.Column(db.Integer, db.ForeignKey('environment.id'), nullable=True)
    atmosphere_id = db.Column(db.Integer, db.ForeignKey('atmosphere.id'), nullable=True)
    surface_map_id = db.Column(db.Integer, db.ForeignKey('surface_map.id'), nullable=True)

    star = db.relationship('Star', backref='planets')
    planet_type = db.relationship('PlanetType', backref='planets')    
    environment = db.relationship('Environment', backref='planets')    
    atmosphere = db.relationship('Atmosphere', backref='planets')    
    surface_map = db.relationship('SurfaceMap', backref='planets')    

    @classmethod
    def generate(cls, **kwargs):
        title = kwargs.get('title')
        star_id = kwargs.get('star_id', 0) 
        image = kwargs.get('image')

        # StarGenerator.sun_list = StarType.query.filter_by(blue=False).all()
        # StarGenerator.blue_sun_list = StarType.query.filter_by(blue=True).all()
        # if star_type:
        #     sun = StarType.query.get(star_type)
        # else:
        #     sun = None
        s = StarGenerator.generate()
        if not title:
            title = "Planet (%s)" % (s.title)
        # print(id + 1, p.planet_type)
        # print(p.margin_left, p.width)
        # print("\tEnvironment:\t\t%s" % (p.environment))
        # print("\tAtmosphere:\t\t%s" % (str(p.atmosphere)))
        # print("\tSurface map available:\t%s" % (p.surface_map))
        # print("\tDay duration:\t\t%s hours" % (p.hours))
        # print("\tGravity:\t\t%s (compared to Earth)" % (p.gravity))
        # print("\tOrbit duration:\t\t%s Earth years" % (p.days))
        # print("\tNumber of moons:\t%s" % (p.moons))
        # print("\tAxial tilt:\t\t%s&#176;" % (p.tilt))
        if not image:
            image = s.image
        planet = Planet(title=title, image=image)
        if star_id:
            planet.star = Star.query.get(star_id)
        return planet
    
    def __repr__(self):
        if self.title is None:
            return "<UNTITLED>"
        else:
            return self.title
        
    def generate_planets(self, star, planet_count=0):
        import random
        if not planet_count:
            planet_count = random.randrange(7) + 4

        earth = False
        for i in range(planet_count):
            p = PlanetGenerator1.generate(i < 6, earth)
            # curPlanet = planet.slice(0, -2)
            if p.planet_type.earth:
                earth = True
            planet = Planet(
                title=str(p.planet_type),
                image=str(p.planet_type),
            )
            star.planets.append(planet)
        return star.planets
        
    @property
    def image_file(self):
        return url_for('static', filename="images/sun27.png")