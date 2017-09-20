from wtforms import StringField, SubmitField

from .models import Campaign


from app.forms import ModelForm


class CampaignForm(ModelForm):
    title = StringField()
    submit = SubmitField('Submit')

    class Meta:
        model = Campaign
