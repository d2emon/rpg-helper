from wtforms import StringField, TextAreaField, SubmitField

from .models import Campaign


from app.forms import ModelForm


class CampaignForm(ModelForm):
    title = StringField()
    description = TextAreaField()    
    submit = SubmitField('Submit')

    class Meta:
        model = Campaign
