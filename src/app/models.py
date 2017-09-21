from flask import request
from flask_sqlalchemy import BaseQuery


from app import app


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