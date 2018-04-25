from app import db
from datetime import datetime


def initialize_database():
    app.logger.info('Database is not created, exec create_all() here.')
    db.create_all()
    data1 = Todo('todo1')
    data2 = Todo('todo2')
    db.session.add(data1)
    db.session.add(data2)
    db.session.commit()


class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column('todo_id', db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    done = db.Column(db.Boolean)
    pub_date = db.Column(db.DateTime)

    def __init__(self, title):
        self.title = title
        self.done = False
        self.pub_date = datetime.utcnow()

    def get_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'done': self.done,
            'pub_date': self.pub_date.strftime('%Y-%m-%d %H:%M'),
        }
