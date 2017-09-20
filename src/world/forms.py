from wtforms import StringField, SubmitField


from app.forms import ModelForm


from world.models import World
from world.models.galaxy import Galaxy, GalaxyName, GalaxyPlacement, GalaxyForm as GalaxyFormModel, GalaxyType


class WorldForm(ModelForm):
    title = StringField()
    submit = SubmitField('Submit')

    class Meta:
        model = World


class GalaxyForm(ModelForm):
    title = StringField()
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