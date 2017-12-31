FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

# Expose port
EXPOSE  5000

# Run supervisor
RUN mkdir -p /etc/supervisor/conf.d/
ADD ./conf/heisen_supervisor.conf /etc/supervisor/conf.d/

# Add main codebase
# RUN cd /code/heisen && python manage.py collectstatic --noinput >> /var/log/collectstatic.log

RUN mkdir -p /var/lib/nginx/cache
RUN chown www-data /var/lib/nginx/cache
RUN chmod 700 /var/lib/nginx/cache

RUN apt-get update
RUN apt-get -yf install supervisor redis-server

CMD ["/usr/bin/supervisord"]
