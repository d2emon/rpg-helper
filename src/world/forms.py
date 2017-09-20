from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms_alchemy import model_form_factory


from world.models import World, Galaxy, GalaxyName


from app import db


BaseModelForm = model_form_factory(FlaskForm)


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session


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