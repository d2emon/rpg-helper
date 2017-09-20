from app import db
from sqlalchemy.sql import func


class GameSession(db.Model):
    """
    Create a Game Session table
    """

    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'))
    real_date = db.Column(db.Date, server_default=func.now(), info={'label': "Real World Date"})
    title = db.Column(db.String(32), info={'label': "Title"})
    description = db.Column(db.UnicodeText(), info={'label': "Description"})

    campaign = db.relationship('Campaign', backref='sessions')

    def __repr__(self):
        if self.title:
            return "%s (%s)" % (self.title, self.real_date)
        return str(self.real_date)
