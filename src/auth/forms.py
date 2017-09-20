from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
# from wtforms.ext.sqlalchemy.fields import QuerySelectField


from app.forms import ModelForm


from .models import User


class LoginForm(ModelForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

    class Meta:
        model = User
        only = ['username', ]


class RegisterForm(ModelForm):
    # case = QuerySelectField(
    #     "Дело",
    #     query_factory=lambda: Case.query.all(),
    #     allow_blank=True,
    # )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    class Meta:
        model = User
        exclude = ['password_hash', ]
