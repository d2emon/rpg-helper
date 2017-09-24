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
    image = db.Column(db.String(32), nullable=True, info={'label': "Image"})
    earth = db.Column(db.Boolean, nullable=True, info={'label': "Earth"})        
    
    @classmethod
    def load_fixture(cls, fixture):
        model = cls(title=str(fixture))
        model.image = str(fixture)
        model.earth = fixture.earth
        return model
                
    @property
    def max_moons(self):
        if self.earth:
            return 5
        else:
            return 40

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
    def generate(cls, near=False, earth=False, **kwargs):
        title = kwargs.get('title')
        star_id = kwargs.get('star_id', 0) 
        image = kwargs.get('image')
        margin = kwargs.get('margin', 0.0)

        # StarGenerator.sun_list = StarType.query.filter_by(blue=False).all()
        # StarGenerator.blue_sun_list = StarType.query.filter_by(blue=True).all()
        # if star_type:
        #     sun = StarType.query.get(star_type)
        # else:
        #     sun = None
        PlanetGenerator1.atmospheres = [None,] + Atmosphere.query.all()
        PlanetGenerator1.combPlanets = PlanetType.query.all()
        PlanetGenerator1.noEarthPlanets = PlanetType.query.all()
        PlanetGenerator1.environments = Environment.query.all()
        PlanetGenerator1.maps = SurfaceMap.query.all()
        p = PlanetGenerator1.generate(near, earth)
        if not title:
            title = "Planet (%s)" % (p.planet_type)
        if not image:
            image = str(p.planet_type)
        m = p.margin_left * p.width * 0.01
        planet = Planet(
            title=title,
            image=image,
            size=p.width,
            from_sun=m + margin,
            day=p.hours,
            year=p.days,
            gravity=p.gravity,
            moons=p.moons,
            tilt=p.tilt,
        )
        planet.atmosphere = p.atmosphere
        planet.planet_type = p.planet_type
        planet.environment = p.environment
        planet.surface_map = p.surface_map
        if star_id:
            planet.star = Star.query.get(star_id)
        return planet
    
    def __repr__(self):
        if self.title is None:
            return "<UNTITLED>"
        else:
            return self.title
        
    def generate_planets(self, star, planet_count=None):
        import random
        if planet_count is None:
            planet_count = random.randrange(7) + 4

        earth = False
        base_margin = 0.0
        for i in range(planet_count):
            planet = self.generate(i < 6, earth, margin=base_margin)
            # curPlanet = planet.slice(0, -2)
            # if p.planet_type.earth:
            #     earth = True
            base_margin = planet.from_sun + planet.size
            star.planets.append(planet)
        return star.planets
        
    @property
    def image_file(self):
        if self.planet_type_id in range(0, 40):
            return url_for('static', filename="images/planet/earthPlanet37.png")
        elif self.planet_type_id in range(40, 120):
            return url_for('static', filename="images/planet/layerPlanet31.png")
        elif self.planet_type_id in range(120, 160):
            return url_for('static', filename="images/planet/terplanet9.png")
        elif self.planet_type_id in range(160, 200):
            return url_for('static', filename="images/planet/moonPlanet14.png")
        elif self.planet_type_id in range(200, 240):
            return url_for('static', filename="images/planet/gasPlanet17.png")
        return url_for('static', filename="images/planet/moonPlanet20.png")