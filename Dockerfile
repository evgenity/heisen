FROM python:2.7
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -yf install supervisor redis-server && rm -rf /var/lib/apt/lists/*

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD frontend /code/frontend
ADD heisen /code/heisen
ADD conf /code/conf

RUN mkdir -p /etc/supervisor/conf.d/
ADD ./conf/heisen_supervisor.conf /etc/supervisor/conf.d/

EXPOSE  5000

CMD ["/usr/bin/supervisord"]
