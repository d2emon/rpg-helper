from flask_wtf import FlaskForm
# from flask.ext.wtf import Form
# from FlaskForm import Form
from wtforms import TextField, TextAreaField
from wtforms.validators import Required, NumberRange


class CharEditForm(FlaskForm):
    charname = TextField('charname', validators = [Required()])
    st = TextField('st', validators = [NumberRange()])
    dx = TextField('dx', validators = [NumberRange()])
    iq = TextField('iq', validators = [NumberRange()])
    ht = TextField('ht', validators = [NumberRange()])

    def load_char(self, c):
        self.charname.data = c.charname
        self.st.data = c.st
        self.dx.data = c.dx
        self.iq.data = c.iq
        self.ht.data = c.ht

    def save_char(self, c):
        c.charname = self.charname.data
        c.st = self.st.data
        c.dx = self.dx.data
        c.iq = self.iq.data
        c.ht = self.ht.data


class FractionEditForm(FlaskForm):
    title = TextField('title', validators = [Required()])
    description = TextAreaField('description')
    weight = TextField('weight', validators = [NumberRange()])
    dx = TextField('dx', validators = [NumberRange()])
    iq = TextField('iq', validators = [NumberRange()])
    ht = TextField('ht', validators = [NumberRange()])

    def load_fraction(self, c):
        self.title.data = c.title
        self.description.data = c.description
        self.weight.data = c.weight

    def save_fraction(self, c):
        c.title = self.title.data
        c.description = self.description.data
        c.weight = self.weight.data
