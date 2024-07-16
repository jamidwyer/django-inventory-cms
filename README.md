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

```
docker exec -t postgres pg_dumpall -c -U     order_by = ['expiration_date']
postgres > dump_`date +%Y-%m-%d"_"%H_%M_%S`.sql
```

### Dev Notes
To avoid wiping your local db every time you rebuild, make sure the migrate lines are commented out in entrypoint.sh.

## Roadmap

### MVP

- query aws db
- persist data across deploys
- fix static files

### Nice to have

- fix test connection
- separate recipe app
- recipe
- rds
- elastic beanstalk
- cache github actions
- ActivityPub
- improve user
- images
- eks
- docker compose override https://docs.docker.com/compose/multiple-compose-files/extends/
- folder structure
- gql and apollo client

## Thank you

https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

https://dev.to/ki3ani/deploying-your-first-dockerized-django-rest-api-on-aws-elastic-beanstalk-a-comprehensive-guide-2m77

https://www.udemy.com/course/django-python-advanced/