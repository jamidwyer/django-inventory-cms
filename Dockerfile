# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat libpq-dev gcc

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
COPY ./scripts /scripts
COPY ./cms /app
RUN pip install -r requirements.txt && \
    adduser --disabled-password --no-create-home django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts
COPY ./scripts /scripts

EXPOSE 8000
ARG DEV=false

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . .

ENV PATH="/scripts:/py/bin:$PATH"

USER django-user

# run entrypoint.sh
CMD ["/run.sh"]

