from app import db
from sqlalchemy.sql import func
from datetime import datetime


class GameSession(db.Model):
    """
    Create a Game Session table
    """

    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'))
    # real_date = db.Column(db.Date, default=datetime.today, server_default=func.now())
    real_date = db.Column(db.Date, server_default=func.now())
    title = db.Column(db.String(32))
    description = db.Column(db.UnicodeText())

    campaign = db.relationship('Campaign', backref='sessions')

    def __repr__(self):
        if self.title:
            return self.title
        return str(self.real_date)
