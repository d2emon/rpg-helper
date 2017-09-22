from flask import url_for


from ..galaxy.models import GeneratorData, Galaxy
 
 
from app import db
from temporary.generator.star import StarGenerator
                

class StarType(GeneratorData, db.Model):
    """
    Create a StarType table
    """
    image = db.Column(db.String(32), nullable=True, info={'label': "Image"})
    blue = db.Column(db.Boolean, nullable=True, info={'label': "Blue"})        

    @classmethod
    def load_fixture(cls, fixture):
        model = cls(
            title=fixture.title,
            image=fixture.image,
            blue=fixture.blue
        )
        return model


class Star(db.Model):
    """
    Create a Galaxy table
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False, info={'label': "Title"})
    image = db.Column(db.String(32), nullable=True, info={'label': "Image"})
    description = db.Column(db.UnicodeText(), info={'label': "Description"})
    galaxy_id = db.Column(db.Integer, db.ForeignKey('galaxy.id'))

    galaxy = db.relationship('Galaxy', backref='stars')

    @classmethod
    def generate(cls, **kwargs):
        title = kwargs.get('title')
        galaxy_id = kwargs.get('galaxy_id', 0) 
        image = kwargs.get('image')
        s = StarGenerator.generate(blue_sun=True)
        # title = cls.generator().generate().title
        if not title:
            title = "Star (%s)" % (s.title)
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
        if not image:
            image = s.image
        star = Star(title=title, image=image)
        if galaxy_id:
            star.galaxy = Galaxy.query.get(galaxy_id)
        return star
    
    def __repr__(self):
        if self.title is None:
            return "<UNTITLED>"
        else:
            return self.title   
        
    @property
    def image_file(self):
        # if self.blue:
        #     return url_for('static', filename="images/sun35.png")
        return url_for('static', filename="images/sun27.png")
        # return "/images/planets/%s.png" % (self.image)