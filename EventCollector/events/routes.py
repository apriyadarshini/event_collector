'''
Created on 30 Jul 2019

@author: Aruna
'''

from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)

from EventCollector.events.utils import  collect_event_source
from EventCollector.events.forms import CollectEventForm
from EventCollector.models import Jobstatus

events = Blueprint('events',__name__)

@events.route('/collect_event/<string:ip>',methods=['GET', 'POST'])
def collect_event(ip):
    form = CollectEventForm()
    if form.validate_on_submit():
        event = form.event.data
        jobid = collect_event_source(event,ip)
        return redirect(url_for('events.job_submitted',jobid=jobid))
    return render_template('collect_event.html',title='Collect Event',form = form)

@events.route('/job_submitted/<jobid>',methods=['GET'])
def job_submitted(jobid):
    job = Jobstatus.query.filter_by(id=jobid).first_or_404()
    return render_template('job_status.html',title='Job Status',job = job)