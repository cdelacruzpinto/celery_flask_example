FROM python:3.7-slim-bullseye

RUN mkdir -p /app
RUN touch /app/__init__.py
RUN apt-get update; apt-get install -y vim nano procps
COPY requirements.txt /app
COPY ./flaskapp /app

WORKDIR /app
RUN python3 -m pip install wheel; python3 -m pip install --upgrade pip; python3 -m pip install -r /app/requirements.txt
#ENV FLASK_APP=fss/fss.py
#ENTRYPOINT ["flask","run","--host=0.0.0.0"]
ENTRYPOINT ["gunicorn", "--worker-class", "gevent", "--bind" ,"0.0.0.0:5000", "wsgi:app", "--workers", "1"]
