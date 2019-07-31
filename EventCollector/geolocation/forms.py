'''
Created on 30 Jul 2019

@author: Aruna
'''

from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField

class GetGeoForm(FlaskForm):
    ip = StringField('IP Address',validators=[DataRequired()])
    submit = SubmitField('Submit')
    
    

class Search(FlaskForm):
    location = StringField('Location',validators=[DataRequired()])
    time1 = StringField('From',validators=[DataRequired()])
    time2 = StringField('To',validators=[DataRequired()])
    submit = SubmitField('Submit') 
    