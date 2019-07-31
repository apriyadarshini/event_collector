'''
Created on 30 Jul 2019

@author: Aruna
'''

from flask import Blueprint, render_template

errors = Blueprint('errors',__name__)

@errors.app_errorhandler(429)
def error_429(error):
    return render_template('errors/429.html'), 429



@errors.app_errorhandler(400)
def error_400(error):
    return render_template('errors/400.html'), 400