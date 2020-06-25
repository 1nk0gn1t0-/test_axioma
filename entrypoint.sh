#!/bin/sh

echo "Waiting for mysql..."

while ! nc -z db 3306; do
    sleep 0.1
done

echo "Mysql started"

python manage.py makemigrations
python manage.py migrate

echo "Starting server"
python manage.py runserver 0.0.0.0:8000