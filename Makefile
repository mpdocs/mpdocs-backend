REGISTRY := "ghcr.io/mpdocs"

up:
	docker compose -f docker-compose.dev.yaml up -d

down:
	docker compose -f docker-compose.dev.yaml down

build:
	docker build -f ./Dockerfile.dev . -t ${REGISTRY}/backend:dev

build-prod:
	docker build --platform=linux/amd64 -f ./Dockerfile . -t ${REGISTRY}/backend:prod

