RUN cd /code/heisen && python scheduler.py >> /var/log/scheduler.log
RUN cd /code/heisen && python manage.py rqscheduler >> /var/log/rqscheduler.log
/usr/bin/supervisord
