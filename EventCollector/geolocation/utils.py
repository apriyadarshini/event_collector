'''
Created on 30 Jul 2019

@author: Aruna
'''

from EventCollector.models import Geolocation
import json
from EventCollector import db
from flask import  current_app, abort

import os

def get_geo_loc(ip):
    import socket
    try:
        socket.inet_aton(ip)
    except socket.error:
        abort(400)
    ipobj = Geolocation.query.filter_by(ipaddr=ip).first()
    if ipobj is None:
        import geoip2.database
        fn = picture_path = os.path.join(current_app.root_path, 'static', "GeoLite2-City.mmdb")
        reader = geoip2.database.Reader(fn)
        response = reader.city(ip)
        geostring = str(response.raw).encode('utf8')
        geoloc = Geolocation(ipaddr=ip,country=response.registered_country.names['en'],geolocjson=geostring)
        db.session.add(geoloc)
        db.session.commit()
        
    