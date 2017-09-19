from app import db
from generator.generator.space.galaxy import GalaxyGenerator


class World(db.Model):
    """
    Create a World table
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    description = db.Column(db.UnicodeText())

    def __repr__(self):
        return self.title


class Galaxy(db.Model):
    """
    Create a Galaxy table
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    description = db.Column(db.UnicodeText())

    @classmethod
    def generate(cls, **kwargs):
        title = kwargs.get('title')
        if not title:
            title = GalaxyGenerator.generate_text()
        return cls(title=title)

    def __repr__(self):
        if self.title is None:
            return "<UNTITLED>"
        else:
            return self.title
