from wtforms import SubmitField


from .models import Campaign


from app.forms import ModelForm


class CampaignForm(ModelForm):
    submit = SubmitField('Submit')

    class Meta:
        model = Campaign
