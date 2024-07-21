FROM python:3.11.4-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat libpq-dev gcc

WORKDIR /app/server

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
COPY . /app/server

EXPOSE 8000
ARG DEV=false
RUN pip install -r requirements.txt && \
    adduser --disabled-password --no-create-home django-user && \
    mkdir /staticfiles && \
    chown -R django-user:django-user /staticfiles && \
    chmod -R 755 /staticfiles

ENV PATH="/scripts:/py/bin:$PATH"

USER django-user

CMD ["./entrypoint.sh"]
