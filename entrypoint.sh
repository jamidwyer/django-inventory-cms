#!/bin/sh

set -e

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py wait_for_db
python manage.py collectstatic --noinput
# The next line wipes the database, so... be careful.
# python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --fake contenttypes
python manage.py spectacular
python manage.py create_groups
gunicorn --config gunicorn_config.py cms.wsgi:application

exec "$@"
