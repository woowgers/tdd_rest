#!/bin/sh

while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  sleep 1
done

pip install -r requirements/dev.txt
python src/manage.py migrate
python src/manage.py runserver 0.0.0.0:3000
