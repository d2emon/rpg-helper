from app import db
from generator.space.galaxy import GalaxyGenerator


from world.models import World


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
        if world_id:
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
        
    @classmethod
    def load_fixture(cls, fixture):
        model = cls(title=str(fixture))
        return model


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