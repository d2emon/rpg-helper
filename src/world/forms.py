from wtforms import SubmitField


from app.forms import ModelForm


from world.models import World
from world.models.galaxy import Galaxy, GalaxyName, GalaxyPlacement, GalaxyForm as GalaxyFormModel, GalaxyType


class WorldForm(ModelForm):
    submit = SubmitField('Submit')

    class Meta:
        model = World


class GalaxyForm(ModelForm):
    submit = SubmitField('Submit')

    class Meta:
        model = Galaxy


class GalaxyNameForm(ModelForm):
    submit = SubmitField('Submit')

    class Meta:
        model = GalaxyName


class GalaxyPlacementForm(ModelForm):
    submit = SubmitField('Submit')

    class Meta:
        model = GalaxyPlacement
        

class GalaxyFormForm(ModelForm):
    submit = SubmitField('Submit')

    class Meta:
        model = GalaxyFormModel        
        

class GalaxyTypeForm(ModelForm):
    submit = SubmitField('Submit')

    class Meta:
        model = GalaxyType                