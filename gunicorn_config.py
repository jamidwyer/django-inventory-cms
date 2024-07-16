bind = "0.0.0.0:8000"
module = "cms.wsgi:application"

workers = 4
worker_connections = 1000
threads = 4

# certfile = "/etc/letsencrypt/live/hord.tech/fullchain.pem"
# keyfile = "/etc/letsencrypt/live/hord.tech/privkey.pem"
