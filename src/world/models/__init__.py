from app import db
from app.models import PagedQuery


class World(db.Model):
    """
    Create a World table
    """
    query_class = PagedQuery

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False, info={'label': "Title"})
    description = db.Column(db.UnicodeText(), info={'label': "Description"})

    def __repr__(self):
        return self.title