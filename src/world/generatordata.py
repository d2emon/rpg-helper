from app import db
        

class GeneratorData:
    """
    Basic class for generator data
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False, info={'label': "Title"})

    def __repr__(self):
        if self.title is None:
            return "<UNTITLED>"
        else:
            return self.title
        
    @classmethod
    def load_fixture(cls, fixture):
        model = cls(title=str(fixture))
        return model
