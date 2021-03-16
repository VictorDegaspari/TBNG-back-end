SHELL := /bin/bash
.ONESHELL:

celery-start-worker:
	source venv/bin/activate
	cd src

	if [ -f .env ]
	then
	export $(cat .env | sed 's/#.*//g' | xargs)
	fi

	celery -A apps.tarefas worker --beat  -l info

database-reset:
	cd src
	rm celerybeat-schedule.db
	rm db.sqlite3

django-create-app:
	source venv/bin/activate
	cd src
	mkdir ./apps/$(app)
	python manage.py startapp $(app) ./apps/$(app)

django-shell:
	source venv/bin/activate 
	cd src
	python manage.py shell

django-make-migrations:
	source venv/bin/activate
	cd src
	python manage.py makemigrations

django-migrate:
	source venv/bin/activate 
	cd src
	python manage.py migrate

django-runserver:
	source venv/bin/activate 
	cd src
	python manage.py runserver

django-load-env:
	source venv/bin/activate
	cd src
	python manage.py loaddata fixtures/dev_env.json

django-test:
	source venv/bin/activate
	cd src
	python manage.py test apps

django-test-wip:
	source venv/bin/activate
	cd src
	python manage.py test --tag=wip apps

browser-open:
	source venv/bin/activate
	python -m webbrowser "http://localhost:8000"

django-start-full:
	source venv/bin/activate
	cd src
	pip install -r requirements.txt
	python manage.py makemigrations
	python manage.py migrate
	python manage.py loaddata fixtures/dev_env.json
	python manage.py runserver

django-sync-db:
	source venv/bin/activate
	cd src
	python manage.py migrate --run-syncdb

docker-clear:
	docker stop $(docker ps -a -q)
	docker rm $(docker ps -a -q)
	docker rmi $(docker images -a -q)

docker-compose-up:
	docker-compose up

docker-restart:
	docker stop $(docker ps -a -q)
	docker rm $(docker ps -a -q)
	docker rmi $(docker images -a -q)
	docker-compose up

docker-stop-all:
	docker stop $(docker ps -a -q)

git-commit: 
	git add -A
	git commit -a -m "$(commit_message)"

git-clear-local-branches:
	git branch | grep -v "main" | xargs git branch -D

pip-install-dependencies:
	source venv/bin/activate
	cd src
	pip install -r requirements.txt	

pip-save-dependencies:
	source venv/bin/activate
	cd src
	pip freeze | grep -v "pkg-resources" > requirements.txt

python-clear-cache:
	find . -regex '^.*\(__pycache__\|\.py[co]\)$' -delete

