from app import db
from generator.space.galaxy import GalaxyGenerator
from temporary.generator.star import StarGenerator


from .world import World


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
        gn = GalaxyName.query.all()
        # if not gn:
        #     gn = GalaxyGenerator.GalaxyGenerator1.galaxy_names[0]
        gp = GalaxyPlacement.query.all()
        # if not gp:
        #     gp = GalaxyGenerator.GalaxyGenerator1.galaxy_names[1]
        gf = GalaxyForm.query.all()
        # if not gf:
        #     gf = GalaxyGenerator.GalaxyGenerator3.galaxy_names[0]
        gt = GalaxyType.query.all()
        # if not gt:
        #     gt = GalaxyGenerator.GalaxyGenerator3.galaxy_names[1]

        g = GalaxyGenerator
        g.GalaxyGenerator1.galaxy_names = [gn, gp]
        g.GalaxyGenerator2.galaxy_names = [gp, gt]
        g.GalaxyGenerator3.galaxy_names = [gf, gt]
        return g

    @classmethod
    def generate(cls, **kwargs):
        title = kwargs.get('title')
        world_id = kwargs.get('world_id', 0) 
        if not title:
            title = cls.generator().generate().title
        g = cls(title=title)
        g.world = World.query.get(world_id)
        return g

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
                

class StarType(GeneratorData, db.Model):
    """
    Create a StarType table
    """
    image = db.Column(db.String(32), nullable=True, info={'label': "Image"})


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
        s = StarGenerator.generate(blue_sun=True)
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
        return Star(title="Star (%s)" % (s.sun_type))
    
    def __repr__(self):
        if self.title is None:
            return "<UNTITLED>"
        else:
            return self.title   
        
    @property
    def image(self):
        return "/images/planets/%s.png" % (self.title)