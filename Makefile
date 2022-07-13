#############################################################################
#                                                                           #
#                       Copyright 2022 Ammar Akbar.                         #
#                           All Rights Reserved.                            #
#                                                                           #
#############################################################################
# Author: Ammar Akbar                                                       #
#                                                                           #
# Make file for running utility commands.                                   #
#############################################################################
flask_run:
	@export FLASK_APP=api/__init__.py && python wsgi.py
build_and_run:
	@docker-compose -f ${yml} up -d --build
build:
	@docker-compose -f ${yml} build
up:
	@docker-compose -f ${yml} up -d
down:
	@docker-compose -f ${yml} down -v
logs:
	@docker-compose -f ${yml} logs -f
ps:
	@docker ps
prune:
	@docker image prune --filter="dangling=true"
init_db:
	@docker-compose -f ${yml} exec flask flask cli init_db
seed_db:
	@docker-compose -f ${yml} exec flask flask cli seed_db
login_db:
	@docker-compose -f ${yml} exec postgres psql --username=${user} --dbname=${db}
check_volume:
	@docker volume inspect powertofly-be-challenge_postgres_data
docker_build:
	@docker build -t ${image}:latest .
docker_run:
	@docker run --env FLASK_ENV=development -p 5000:5000 ${image}:latest
isort:
	@isort -c .
flake8:
	@flake8
