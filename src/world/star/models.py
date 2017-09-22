from ..galaxy.models import GeneratorData, Galaxy
 
 
from app import db
from temporary.generator.star import StarGenerator
                

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
    def generate(cls, **kwargs):
        title = kwargs.get('title')
        galaxy_id = kwargs.get('galaxy_id', 0) 
        if not title:
            s = StarGenerator.generate(blue_sun=True)
            # title = cls.generator().generate().title
            title = "Star (%s)" % (s.sun_type)
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
        star = Star(title=title)
        if galaxy_id:
            star.galaxy = Galaxy.query.get(galaxy_id)
        return star
    
    def __repr__(self):
        if self.title is None:
            return "<UNTITLED>"
        else:
            return self.title   
        
    @property
    def image(self):
        return "/images/planets/%s.png" % (self.title)