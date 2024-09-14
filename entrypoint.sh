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
yes | python manage.py makemigrations --noinput
python manage.py migrate --fake
python manage.py spectacular
gunicorn --config gunicorn_config.py cms.wsgi:application

exec "$@"
