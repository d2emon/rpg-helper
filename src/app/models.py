from flask import request
from flask_sqlalchemy import BaseQuery


from app import app


class PagedQuery(BaseQuery):
    def paged(self, page_var='page', **kwargs):
        '''
        Return block data for user or -1 if not exist
        '''
        try:
            page = int(request.args.get(page_var))
        except (ValueError, TypeError):
            page = 1

        count = kwargs.get('count')
        if count is None:
            count = app.config.get('RECORDS_ON_PAGE')

        return self.paginate(page, count)
