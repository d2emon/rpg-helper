from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
# from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms_alchemy import model_form_factory


from .models import User


from app import db


BaseModelForm = model_form_factory(FlaskForm)


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session


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
