# hord-cms

A Django CMS to serve food source data.

## Dev

In root directory:
`python3 -m venv venv`

`source hordcms/bin/activate`

`pip install -r requirements.txt`

`docker compose up -d`

(Ideally this will be saved somehow?)
`cd cms && createsuperuser`

`./manage.py runserver`

http://127.0.0.1:8000/

http://127.0.0.1:8000/admin/login/?next=/admin/

- get items by user
    - https://www.django-rest-framework.org/api-guide/filtering/
    http://127.0.0.1:8000/inventoryItems/?user_id=5


- save database
docker exec -t postgres pg_dumpall -c -U postgres > dump_`date +%Y-%m-%d"_"%H_%M_%S`.sql

## TODO

### MVP

- save on github!
- sort by expiration date

### Nice to have

- launch
- separate recipe app
- recipe
- ActivityPub
- improve dev setup
    - dockerize https://stackoverflow.com/questions/55483781/how-to-create-postgres-database-and-run-migration-when-docker-compose-up
- get env settings in correct place
- improve user
- folder structure
- gql and apollo client
