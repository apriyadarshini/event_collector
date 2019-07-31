'''
Created on 30 Jul 2019

@author: Aruna
'''

from EventCollector import db
from datetime import datetime



class Geolocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ipaddr = db.Column(db.String(20),unique = True, nullable = False)
    country = db.Column(db.String(120),unique = True, nullable = False)
    geolocjson = db.Column(db.String(300), nullable = False)
    events = db.relationship('Events',backref='generator',lazy=True)
    
    
    def __repr__(self):
        return f"Geolocation('{self.ipaddr}','{self.country}')"
    
    
class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datecollected = db.Column(db.DateTime,nullable = False,default = datetime.utcnow)
    time_stamp = db.Column(db.DateTime,nullable = False)
    host = db.Column(db.String(120), nullable = False)
    source = db.Column(db.String(200), nullable = False)
    name = db.Column(db.String(120), nullable = False)
    fields = db.Column(db.String(500), nullable = False)
    ip_address = db.Column(db.Integer, db.ForeignKey('geolocation.id'))
    
    
    def __repr__(self):
        return f"Events('{self.title}','{self.time}')"
    
class Jobstatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), nullable = False)
    date = db.Column(db.DateTime,nullable = False,default = datetime.utcnow)
    
    def __repr__(self):
        return f"Jobstatus('{self.id}','{self.status}')"
    
    
  