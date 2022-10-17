FROM python:3.10.7

ENV END_POINT=${END_POINT}
ENV API_PORT=${API_PORT}

COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

VOLUME /app
WORKDIR /app

EXPOSE ${API_PORT}
