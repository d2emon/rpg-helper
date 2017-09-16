from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms_alchemy import model_form_factory


from .models import Campaign


from app import db


BaseModelForm = model_form_factory(FlaskForm)


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session


class CampaignForm(ModelForm):
    submit = SubmitField('Submit')

    class Meta:
        model = Campaign
