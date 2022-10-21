FROM python:3.10.7

COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

VOLUME /app
WORKDIR /app

EXPOSE ${CONSUMER_PORT}