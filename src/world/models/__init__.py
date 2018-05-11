from app import db
from app.models import PagedQuery

import random


class World(db.Model):
    """
    Create a World table
    """
    query_class = PagedQuery

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False, info={'label': "Title"})
    description = db.Column(db.UnicodeText(), info={'label': "Description"})
    img = db.Column(db.String(32), info={'label': "Image"})

    def __repr__(self):
        return self.title

    @classmethod
    def load_fixture(cls, fixture):
        model = cls(
            title=fixture.title,
            img=fixture.img,
        )
        return model

    @property
    def dummy_img(self):
        url = "https://loremflickr.com/400/300/"
        return "{}?{}".format(url, random.random())

    def img_path(self, path="/static/images/world"):
        if self.img is None:
            return self.dummy_img
        return "{}/{}".format(path, self.img)

    def toDict(self, path="/static/images/world"):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'img': self.img_path(path),
        }
