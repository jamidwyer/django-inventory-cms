# hord-cms

A Django CMS to serve food source data.

## Dev

In root directory:
`docker compose up --build`

http://127.0.0.1:8000/

http://127.0.0.1:8000/admin


- get items by user
    - https://www.django-rest-framework.org/api-guide/filtering/
    http://127.0.0.1:8000/inventoryItems/?user_id=5

- create superuser

`docker compose run web python manage.py createsuperuser`

- save database
docker exec -t postgres pg_dumpall -c -U     order_by = ['expiration_date']
postgres > dump_`date +%Y-%m-%d"_"%H_%M_%S`.sql

## Deploy

Change tag in dockerrun.aws.json.

`docker build -t hord .`

`docker tag hord:latest <your dockerhub username>/hord:latest`

`docker push <your dockerhub username>/hord:latest`

`eb deploy hord-dev`

## Roadmap

### MVP

- deploy to elastic beanstalk
- get env settings in correct place
- persist data across deploys

### Nice to have

- separate recipe app
- recipe
- ActivityPub
- improve dev setup
    - dockerize https://stackoverflow.com/questions/55483781/how-to-create-postgres-database-and-run-migration-when-docker-compose-up
- improve user
- eks
- folder structure
- gql and apollo client

## Thank you

https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

https://dev.to/ki3ani/deploying-your-first-dockerized-django-rest-api-on-aws-elastic-beanstalk-a-comprehensive-guide-2m77
