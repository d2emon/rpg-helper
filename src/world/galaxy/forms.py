from wtforms import StringField, TextAreaField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField


from app.forms import ModelForm


from world.models import World
from .models import Galaxy, GalaxyName, GalaxyPlacement, GalaxyForm as GalaxyFormModel, GalaxyType, StarType, Star


class GalaxyForm(ModelForm):
    title = StringField()
    world = QuerySelectField(
        query_factory=lambda: World.query.all(),
        allow_blank=True,
    )
    description = TextAreaField()
    submit = SubmitField('Submit')

    class Meta:
        model = Galaxy


class GalaxyNameForm(ModelForm):
    title = StringField()
    submit = SubmitField('Submit')

    class Meta:
        model = GalaxyName


class GalaxyPlacementForm(ModelForm):
    title = StringField()
    submit = SubmitField('Submit')

    class Meta:
        model = GalaxyPlacement
        

class GalaxyFormForm(ModelForm):
    title = StringField()
    submit = SubmitField('Submit')

    class Meta:
        model = GalaxyFormModel        
        

class GalaxyTypeForm(ModelForm):
    title = StringField()
    submit = SubmitField('Submit')

    class Meta:
        model = GalaxyType                
        

class StarTypeForm(ModelForm):
    title = StringField()
    image = StringField()
    submit = SubmitField('Submit')

    class Meta:
        model = StarType                

class StarForm(ModelForm):
    title = StringField()
    galaxy = QuerySelectField(
        query_factory=lambda: Galaxy.query.all(),
        allow_blank=True,
    )
    description = TextAreaField()
    submit = SubmitField('Submit')

    class Meta:
        model = Star