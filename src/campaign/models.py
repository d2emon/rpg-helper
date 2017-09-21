from app import db


class Campaign(db.Model):
    """
    Create a Campaign table
    """

    id = db.Column(db.Integer, primary_key=True)
    # gs_id = Column(Integer, ForeignKey('game_system.id'))
    title = db.Column(db.String(32), info={'label': "Title"})
    description = db.Column(db.UnicodeText(), info={'label': "Description"})
    # characters = db.relationship("GameCharacter")

    def __repr__(self):
        return self.title