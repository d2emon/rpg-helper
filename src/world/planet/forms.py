from wtforms import StringField, TextAreaField, IntegerField, BooleanField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField


from app.forms import ModelForm


from ..star.models import Star
from .models import Planet


# class StarTypeForm(ModelForm):
#     title = StringField()
#     image = StringField()
#     blue = BooleanField()
#     submit = SubmitField('Submit')

#     class Meta:
#         model = StarType                

class PlanetForm(ModelForm):
    title = StringField()
    image = StringField()
    size = StringField()
    from_sun = StringField()
    day = StringField()
    year = StringField()
    gravity = StringField()
    moons = IntegerField()
    tilt = StringField()
    star = QuerySelectField(
        query_factory=lambda: Star.query.all(),
        allow_blank=True,
    )
    # planet_type = QuerySelectField(
    #     query_factory=lambda: Galaxy.query.all(),
    #     allow_blank=True,
    # )
    # environment = QuerySelectField(
    #     query_factory=lambda: Galaxy.query.all(),
    #     allow_blank=True,
    # )
    # atmosphere = QuerySelectField(
    #     query_factory=lambda: Galaxy.query.all(),
    #     allow_blank=True,
    # )
    # surface_map = QuerySelectField(
    #     query_factory=lambda: Galaxy.query.all(),
    #     allow_blank=True,
    # )
    description = TextAreaField()
    submit = SubmitField('Submit')


    class Meta:
        model = Planet