from app import db
from generator.space.galaxy import GalaxyGenerator


class Galaxy(db.Model):
    """
    Create a Galaxy table
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    description = db.Column(db.UnicodeText())
    world_id = db.Column(db.Integer, db.ForeignKey('world.id'))

    world = db.relationship('World', backref='galaxies')
    
    @classmethod
    def generator(cls):
        g = GalaxyGenerator
        g.GalaxyGenerator1.galaxy_names[0] = GalaxyName.query.all()
        g.GalaxyGenerator2.galaxy_names[1] = GalaxyType.query.all()
        g.GalaxyGenerator3.galaxy_names[1] = GalaxyType.query.all()
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
    title = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        if self.title is None:
            return "<UNTITLED>"
        else:
            return self.title

class GalaxyName(GeneratorData, db.Model):
    """
    Create a GalaxyName table
    """
        

class GalaxyType(GeneratorData, db.Model):
    """
    Create a GalaxyType table
    """