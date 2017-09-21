from wtforms import StringField, TextAreaField, DateField, SubmitField


from app.forms import ModelForm


from .models import GameSession


class GameSessionForm(ModelForm):
    title = StringField()
    real_date = DateField()
    description = TextAreaField()
    submit = SubmitField('Submit')

    class Meta:
        model = GameSession