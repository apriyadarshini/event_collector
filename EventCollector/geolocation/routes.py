'''
Created on 30 Jul 2019

@author: Aruna
'''
from flask import render_template, url_for, flash, redirect, request, Blueprint
from EventCollector.geolocation.utils import  get_geo_loc
from EventCollector.geolocation.forms import GetGeoForm, Search
from EventCollector.models import Geolocation, Events
geolocation = Blueprint('geolocation',__name__)

@geolocation.route('/',methods=['GET', 'POST'])
@geolocation.route('/get_geoloc',methods=['GET', 'POST'])
def get_geoloc():
    form = GetGeoForm()
    if form.validate_on_submit():
        ip = form.ip.data
        get_geo_loc(ip)
        return redirect(url_for('geolocation.get_geoloc_ip',ip=ip))
    return render_template('get_geoloc.html',title='Get GeoLocation',form = form)


@geolocation.route('/get_geoloc/<string:ip>',methods=['GET', 'POST'])
def get_geoloc_ip(ip):
    geoloc = Geolocation.query.filter_by(ipaddr=ip).first_or_404()
    return render_template('get_geoloc_ip.html',title='GeoLocation',geoloc=geoloc)

@geolocation.route('/search',methods=['GET', 'POST'])
def search():
    form = Search()
    if form.validate_on_submit():
        location = form.location.data
        t1 = form.time1.data
        t2 = form.time2.data
        return redirect(url_for('geolocation.search_result',location=location,t1=t1,t2=t2))
    return render_template('search_query.html',title='search',form = form)

@geolocation.route('/search_result/<string:location>/<t1>/<t2>',methods=['GET'])
def search_result(location,t1,t2):
    sch = Geolocation.query.filter_by(country=location).join(Events).filter(Events.time_stamp>t1,Events.time_stamp<t2)
    if sch is None:
        sch = 'nodata'
    return render_template('search_result.html',title='Search Result',sch = sch)
    
