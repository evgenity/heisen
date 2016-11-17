# Set the base image to Ubuntu
FROM    ubuntu
ENV PYTHONUNBUFFERED 1

# Define working directory
RUN mkdir /code
WORKDIR /code

# File Author / Maintainer
MAINTAINER Evgeni Bikov

RUN apt-get update
RUN apt-get -yf install \
	build-essential \
	apt-utils \
	dpkg-dev \
	libc6-dev \
	g++ \
    curl \
    python \
    nodejs \
    nginx \
    vim \
    nano\
    python-pip \
    python-dev \
    build-essential \
    openssh-server \
    supervisor \
    mlocate \
    cron

# Install pip requirements
ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Start nginx
RUN rm /etc/nginx/sites-enabled/default
ADD ./conf/heisen_nginx.conf /etc/nginx/sites-enabled/
# RUN service nginx start

# Expose port
EXPOSE  80 443

# Run supervisor
RUN mkdir -p /etc/supervisor/conf.d/
ADD ./conf/heisen_supervisor.conf /etc/supervisor/conf.d/

# Adding SSL-keys
RUN mkdir -p /etc/letsencrypt/
ADD ./letsencrypt/ /etc/letsencrypt/

# Add main codebase
ADD . /code/

RUN python /code/heisen/manage.py collectstatic --noinput
#RUN python /code/heisen/manage.py crontab add home.cron.updater
#RUN service cron restart
CMD ["/usr/bin/supervisord"]
