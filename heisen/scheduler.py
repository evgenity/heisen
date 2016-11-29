import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "heisen.settings")
import django_rq
from home.cron import updater
from home.backup import init_and_update
from datetime import datetime
from django_rq import job

scheduler = django_rq.get_scheduler('default')


job = scheduler.schedule(
    scheduled_time=datetime.utcnow(), # Time for first execution, in UTC timezone
    func=updater,                     # Function to be queued
    args=[],             # Arguments passed into function when executed
    kwargs={},         # Keyword arguments passed into function when executed
    interval=180,                   # Time before the function is called again, in seconds
    repeat=None                      # Repeat this number of times (None means repeat forever)
)

backup = scheduler.schedule(
    scheduled_time=datetime.utcnow(), # Time for first execution, in UTC timezone
    func=init_and_update,                     # Function to be queued
    args=[],             # Arguments passed into function when executed
    kwargs={},         # Keyword arguments passed into function when executed
    interval=12*60*60, #12hours               # Time before the function is called again, in seconds
    repeat=None                      # Repeat this number of times (None means repeat forever)
)
