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


- save database
docker exec -t postgres pg_dumpall -c -U postgres > dump_`date +%Y-%m-%d"_"%H_%M_%S`.sql

## Deploy

Change tag in dockerrun.aws.json.

`docker build -t hord .`

`docker tag hord:latest <your dockerhub username>/hord:latest`

`docker push <your dockerhub username>/hord:latest`

`eb deploy hord-dev`

## Roadmap

### MVP

- sort by expiration date
- deploy to elastic beanstalk

### Nice to have

- separate recipe app
- recipe
- ActivityPub
- improve dev setup
    - dockerize https://stackoverflow.com/questions/55483781/how-to-create-postgres-database-and-run-migration-when-docker-compose-up
- get env settings in correct place
- improve user
- eks
- folder structure
- gql and apollo client

## Thank you

https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
