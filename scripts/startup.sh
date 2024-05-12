#!/bin/bash

poetry run python manage.py migrate
poetry run gunicorn service.wsgi:application --bind 0.0.0.0:8000
