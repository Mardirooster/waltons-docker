#!/bin/bash

source dm-copy.sh mycms-dev web /mnt/sda1/var/lib/docker/volumes/web/_data/

docker-machine ssh mycms-dev docker exec dockertest_web_1 python manage.py collectstatic --noinput
docker-machine ssh mycms-dev docker exec dockertest_web_1 python manage.py makemigrations
docker-machine ssh mycms-dev docker exec dockertest_web_1 python manage.py migrate
