FROM python:3.10-slim AS builder

ARG EXPORT_FLAG=


FROM python:3.10-slim

WORKDIR /app

RUN groupadd -g 10000 app && \
  useradd -g app -d /app -u 10000 app && \
  chown app:app /app && \
  apt-get update && \
  apt install -y gcc libpq-dev git gettext make && \
  pip install --upgrade pip &&\
  pip install 'django-phonenumber-field[phonenumberslite]' 
  #pip3 install django-phonenumber-field[phonenumbers] 

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt 
    #pip install django-phonenumber-field[phonenumberslite]
COPY . .

RUN django-admin compilemessages 

USER app

EXPOSE 8080
