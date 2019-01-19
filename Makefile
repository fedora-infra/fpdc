include .env

build:
	sudo podman build -t fpdc-web $(CURDIR)

down:
	sudo podman pod rm -f fpdc-dev

logs-db:
	sudo podman logs database

logs-web:
	sudo podman logs fpdc-web

ps:
	sudo podman ps -pa

prune:
	sudo podman volume rm -f pgdata

up:
	sudo podman pod create --name fpdc-dev -p 8000:8000
	sudo podman run --name fpdc-web --pod fpdc-dev -dt -e OIDC_RP_CLIENT_ID=$(OIDC_RP_CLIENT_ID) -e OIDC_RP_CLIENT_SECRET=$(OIDC_RP_CLIENT_SECRET) -e DJANGO_SETTINGS_MODULE=fpdc.settings.base -v $(CURDIR):/code fpdc-web
	sudo podman run --name database --pod fpdc-dev -dt -e PGDATA=/var/lib/postgresql/data/pgdata -v pgdata:/var/lib/postgresql/data/pgdata  postgres

shell:
	sudo podman exec -it fpdc-web bash

start:
	sudo podman pod start fpdc-dev

stop:
	sudo podman pod stop fpdc-dev
