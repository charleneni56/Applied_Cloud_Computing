# Applied_Cloud_Computing

docker network create mynetwork

cd db
docker build -t my_db .
docker run --name mydb --network mynetwork -itd -p5432:5432 my_db

cd ..
cd dba

docker build -t my_dba .
docker run --name mydba --network mynetwork -p8081:80 -d my_dba 

Localhost:8081
#admin@admin.com
#pass
Add Server: name/host mydb, user=root, password=pass, 

cd ..

docker build -t my_django .
docker run -it -p8000:8000 -v $(pwd)/app:/app my_django /bin/bash
django-admin startproject app
Exit

docker run -it -p8000:8000 --network mynetwork -v $(pwd)/app:/app my_django /bin/bash
python manage.py migrate
python manage.py createsuperuser
#user=root
#email=a@a.com
#password=pass

localhost:8000


#connect postpre in settings.py file
## settings.py file 
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'web',
        'USER': 'root',
        'PASSWORD': 'pass',
        'HOST': 'mydb',
        'PORT': 5432,
  ##  }
##}

cd app
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
Localhost:8081
#updates to tables 
