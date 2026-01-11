SHELL := /bin/bash

include .env
export

.PHONY: run-docker stop-docker logs-docker create-migrations run-migrations run

run-docker:
	docker compose up -d

stop-docker:
	docker compose down

logs-docker:
	docker compose logs -f

create-migrations:
	@if [ -z "$(d)" ]; then echo "Uso: make create-migrations d=\"nome_da_migration\""; exit 1; fi
	alembic revision --autogenerate -m "$(d)"

run-migrations:
	alembic upgrade head

run:
	uvicorn app.main:app --host $${APP_HOST:-127.0.0.1} --port $${APP_PORT:-8000} --reload
