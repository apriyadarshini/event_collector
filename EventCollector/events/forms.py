'''
Created on 30 Jul 2019

@author: Aruna
'''

from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField

class CollectEventForm(FlaskForm):
    event = StringField('Enter the event',validators=[DataRequired()])
    submit = SubmitField('Submit')
    