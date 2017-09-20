from wtforms import SubmitField


from app.forms import ModelForm


from .models import GameSession


class GameSessionForm(ModelForm):
    submit = SubmitField('Submit')

    class Meta:
        model = GameSession