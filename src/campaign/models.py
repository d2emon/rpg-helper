from flask import request
from flask_sqlalchemy import BaseQuery


from app import app, db


class PagedQuery(BaseQuery):
    def paged(self, page_var='page'):
        '''
        Return block data for user or -1 if not exist
        '''
        try:
            page = int(request.args.get(page_var))
        except (ValueError, TypeError):
            page = 1
            
        return self.paginate(page, app.config.get('RECORDS_ON_PAGE'))


class Campaign(db.Model):
    """
    Create a Campaign table
    """
    query_class = PagedQuery

    id = db.Column(db.Integer, primary_key=True)
    # gs_id = Column(Integer, ForeignKey('game_system.id'))
    title = db.Column(db.String(32), info={'label': "Title"})
    description = db.Column(db.UnicodeText(), info={'label': "Description"})
    # characters = db.relationship("GameCharacter")

    def __repr__(self):
        return self.title