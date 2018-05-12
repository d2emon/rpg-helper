from app import db
from app.models import PagedQuery

# import random


class Gender(db.Model):
    """
    Create a Genders table
    """
    query_class = PagedQuery

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False, info={'label': "Title"})

    def __repr__(self):
        return self.title

class Title(db.Model):
    """
    Create a Medieval Title table
    """
    query_class = PagedQuery

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False, info={'label': "Title"})
    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'), nullable=True)

    gender = db.relationship('Gender')

    def __repr__(self):
        return self.title

    @classmethod
    def load_fixture(cls, fixture):
        model = cls(title=str(fixture))
        model.title = str(fixture)
        model.gender_id = fixture.gender
        return model


class Name(db.Model):
    """
    Create a Medieval Name table
    """
    query_class = PagedQuery

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, info={'label': "Name"})
    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'), nullable=True)

    gender = db.relationship('Gender')

    def __repr__(self):
        return self.name

    @classmethod
    def load_fixture(cls, fixture):
        model = cls(name=str(fixture))
        model.name = str(fixture)
        model.gender_id = fixture.gender
        return model


class GameCharacter(db.Model):
    """
    Create a Game Character table
    """
    query_class = PagedQuery

    id = db.Column(db.Integer, primary_key=True)
    title_id = db.Column(db.Integer, db.ForeignKey('title.id'), nullable=True)
    name = db.Column(db.String(32), nullable=False, info={'label': "Name"})
    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'), nullable=True)

    title = db.relationship('Title')
    sex = db.relationship('Gender')

    def __repr__(self):
        return "{} {}".format(self.title, self.name)
