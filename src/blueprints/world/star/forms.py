from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField


from app.forms import ModelForm


from ..galaxy.models import Galaxy
from .models import StarType, Star


class StarTypeForm(ModelForm):
    title = StringField()
    image = StringField()
    blue = BooleanField()
    submit = SubmitField('Submit')

    class Meta:
        model = StarType                

class StarForm(ModelForm):
    title = StringField()
    image = StringField()
    star_type = QuerySelectField(
        query_factory=lambda: StarType.query.all(),
        allow_blank=True,
    )
    galaxy = QuerySelectField(
        query_factory=lambda: Galaxy.query.all(),
        allow_blank=True,
    )
    description = TextAreaField()
    submit = SubmitField('Submit')

    class Meta:
        model = Star