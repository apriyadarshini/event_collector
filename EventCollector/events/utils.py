'''
Created on 30 Jul 2019

@author: Aruna
'''

from EventCollector import db
from EventCollector.models import Jobstatus
from flask import abort

def collect_event_source(event,ip):
    jobids = Jobstatus.query.filter_by(status='SUBMITTED')
    if jobids.count() == 5:
        abort(429)
    geoloc = Jobstatus(status='SUBMITTED')
    db.session.add(geoloc)
    db.session.commit()
    jobid = Jobstatus.query.filter_by(status='SUBMITTED').order_by(Jobstatus.date.desc()).first()
    if event == 'ssh attack':
        pass 
     
    else:
        abort(400)
    return jobid.id
