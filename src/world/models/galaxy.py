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