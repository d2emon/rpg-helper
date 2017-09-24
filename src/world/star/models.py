from flask import url_for


from app import db
from generator.space.star import StarGenerator
from ..generatordata import GeneratorData
from ..galaxy.models import Galaxy
                

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
    star_type_id = db.Column(db.Integer, db.ForeignKey('star_type.id'), nullable=True)

    galaxy = db.relationship('Galaxy', backref='stars')
    star_type = db.relationship('StarType', backref='stars')

    @classmethod
    def generate(cls, **kwargs):
        title = kwargs.get('title')
        galaxy_id = kwargs.get('galaxy_id', 0) 
        image = kwargs.get('image')
        star_type = kwargs.get('star_type') 

        StarGenerator.sun_list = StarType.query.filter_by(blue=False).all()
        StarGenerator.blue_sun_list = StarType.query.filter_by(blue=True).all()
        if star_type:
            sun = StarType.query.get(star_type)
        else:
            sun = None
        s = StarGenerator.generate(blue_sun=True, sun=sun)
        # title = cls.generator().generate().title
        if not title:
            title = "Star (%s)" % (s.title)
        if not image:
            image = s.image
        star = Star(title=title, image=image)
        if s.star_type:
            star.star_type_id = s.star_type.id
        if star_type:
            star.star_type = s.star_type
        if galaxy_id:
            star.galaxy = Galaxy.query.get(galaxy_id)
        # star.generate_planets(len(s.planets))
        return star
    
    def __repr__(self):
        if self.title is None:
            return "<UNTITLED>"
        else:
            return self.title
        
    @property
    def blue(self):
        if not self.star_type:
            return False
        return self.star_type.blue   
        
    @property
    def image_file(self):
        if self.blue:
            return url_for('static', filename="images/star/sun35.png")
        return url_for('static', filename="images/star/sun27.png")
        # return "/images/planets/%s.png" % (self.image)