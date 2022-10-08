FROM python

COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

VOLUME /app
WORKDIR /app

EXPOSE 8000


# touch text.txt ##touch means creating a file
# rm text.txt

# python /app/app/manage.py migrate
# python /app/app/manage.py runserver 0.0.0.0:8000