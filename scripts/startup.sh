#!/bin/bash

poetry run python manage.py migrate
poetry run gunicorn service.wsgi:application -w 4 --bind 0.0.0.0:8000
