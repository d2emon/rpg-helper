from app import db


class World(db.Model):
    """
    Create a World table
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False, info={'label': "Title"})
    description = db.Column(db.UnicodeText(), info={'label': "Description"})

    def __repr__(self):
        return self.title