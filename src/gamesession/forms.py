from wtforms import StringField, SubmitField


from app.forms import ModelForm


from .models import GameSession


class GameSessionForm(ModelForm):
    title = StringField()
    submit = SubmitField('Submit')

    class Meta:
        model = GameSession