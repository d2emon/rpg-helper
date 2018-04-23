#! /usr/bin/env python
# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField


class CampaignForm(FlaskForm):
    title = StringField("Название", validators=[DataRequired()])
   
    
class SessionForm(FlaskForm):
    title = StringField("Заголовок")
    real_date = DateField('Реальная дата', format='%Y-%m-%d')    
    world_date = DateField('Игровая дата', format='%Y-%m-%d')
    description = TextAreaField('Описание')
            