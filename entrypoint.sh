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
# python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate

uwsgi --socket :8000 --workers 4 --master --enable-threads --module cms.wsgi

exec "$@"
