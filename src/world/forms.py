from wtforms import StringField, TextAreaField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField


from app.forms import ModelForm


from world.models import World
from world.models.galaxy import Galaxy, GalaxyName, GalaxyPlacement, GalaxyForm as GalaxyFormModel, GalaxyType, Star


class WorldForm(ModelForm):
    title = StringField()
    description = TextAreaField()    
    submit = SubmitField('Submit')

    class Meta:
        model = World


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