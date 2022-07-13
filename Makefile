update:
	@pip install --upgrade pip

install:
	@pip install -r services/web/requirements.txt

install-dev:
	@pip install -r requirements-dev.txt

run:
	@cd services/web/ && gunicorn -b 0.0.0.0:5000 manage:app

test:
	@python -m pytest

pre-commit:
	@pre-commit install

initial-tag:
	@git tag -a -m "Initial tag." v0.0.1

init-cz:
	@cz init

bump-tag:
	@cz bump --check-consistency --changelog

start-db-containers:
	@sudo docker-compose -f services/database/database-compose.yml up --build -d

stop-db-containers:
	@sudo docker-compose -f services/database/database-compose.yml down -v

create-db:
	@python services/web/manage.py create_db

seed-db:
	@python services/web/manage.py seed_db

test-local:
	@curl localhost:5000/
	@curl localhost:5000/users
