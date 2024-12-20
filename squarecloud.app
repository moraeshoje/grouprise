DISPLAY_NAME=Webhook Bot
MAIN=main.py
VERSION=recommended
MEMORY=512
AUTORESTART=true
DESCRIPTION=Servidor de webhook para o bot
START=gunicorn -b 0.0.0.0:5000 main:app
SUBDOMAIN=grouprise
