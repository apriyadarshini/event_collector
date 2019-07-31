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
        pass #This section has not been implemented as the requirement regarding 
    #what kind of events needs to be collected was not given
    #currently I am assuming event would be like a name predefined by us and given to the customer.
    #e.g. 'ssh attack' and this is what the customer would enter in the text box.
    #If that is the way customer enters events, this block of code runs that part of code in the background 
    #(in this case doing a grep on /var/log/auth.log for "Failed password" text) and updates our events table with the data. This also updates the Jobstatus table's status column to 
    #'COMPLETED' once the events are collected.
    #This is again under the assumption that we have the credentials of the system whose ip is passed by the user
     
    else:
        abort(400)
    return jobid.id