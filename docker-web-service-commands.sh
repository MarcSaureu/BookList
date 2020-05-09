#!/bin/sh

python manage.py runserver

gunicorn --bind 0.0.0.0:${DJANGO_PORT} skeleton.wsgi:application
