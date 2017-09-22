from wtforms import StringField, TextAreaField, SubmitField


from app.forms import ModelForm


from .models import World


class WorldForm(ModelForm):
    title = StringField()
    description = TextAreaField()    
    submit = SubmitField('Submit')

    class Meta:
        model = World