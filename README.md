settin up the website.

    docker-machine create -d virtualbox mycms-dev

    eval "$(docker-machine env mycms-dev)"

    docker-compose build

now sort out the stuff on the machine

    docker-machine ssh mycms-dev

    docker exec -it FOLDERNAME_postgres_1 bash

    psql -U postgres

    CREATE USER mycms_user WITH PASSWORD 'Mycm$_Pa$$';

    ALTER USER mycms_user SUPERUSER;

    CREATE DATABASE mycms WITH OWNER = mycms_user;

    docker exec -it djangocmsdocker_web_1 bash

    python manage.py collectstatic --noinput

    python manage.py migrate

    python manage.py createsuperuser

note: to update the files on the web-container, run machine-update.sh from the web folder