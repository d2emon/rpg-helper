from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField


from app.forms import ModelForm


from ..galaxy.models import Galaxy
from .models import StarType, Star


class StarTypeForm(ModelForm):
    title = StringField()
    image = StringField()
    submit = SubmitField('Submit')
    blue = BooleanField()

    class Meta:
        model = StarType                

class StarForm(ModelForm):
    title = StringField()
    image = StringField()
    galaxy = QuerySelectField(
        query_factory=lambda: Galaxy.query.all(),
        allow_blank=True,
    )
    description = TextAreaField()
    submit = SubmitField('Submit')

    class Meta:
        model = Star