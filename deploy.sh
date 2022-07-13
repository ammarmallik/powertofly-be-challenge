#!/bin/bash
#############################################################################
#                                                                           #
#                       Copyright 2022 Ammar Akbar.                         #
#                           All Rights Reserved.                            #
#                                                                           #
#############################################################################
# Author: Ammar Akbar                                                       #
#                                                                           #
# Deploy the containerized Flask API on Heroku.                             #
#############################################################################
if [ $# -eq 0 ]; then
    echo 'Please pass the repository name on hub.docker.com.'
    exit 90
fi

if [ "$2" != "development" ] && [ "$2" != "production" ]; then
	echo "Invalid environment. Choose between development|production."
	exit 91
fi
#############################################################################

directory=$(dirname "$0")
pushd "$directory" &> /dev/null || exit 80

IMAGE_NAME="powertofly-be-challenge_flask"
REPO_NAME=$1

echo "===============================Docker-Compose Build & Run=================================="
make build_and_run yml=docker-compose.yml || exit 2

echo "===============================Docker CLI Login=================================="
docker login || exit 3

echo "===============================Tag Latest Build=================================="
docker tag $IMAGE_NAME:latest ammarmallik/$REPO_NAME:latest || exit 4

echo "===============================Push Build to hub.docker.com=================================="
docker push ammarmallik/$REPO_NAME:latest || exit 5

echo "===============================Login Heroku=================================="
heroku login || exit 6

echo "===============================Login registry.heroku.com using docker=================================="
docker login --username=_ --password=$(heroku auth:token) registry.heroku.com || exit 7

echo "===============================Push Docker Image to Heroku=================================="
heroku container:push web || exit 8

echo "===============================Set Environment Variables=================================="
if [ "$2" == "production" ];then
    xargs -a ./.env/.env.prod -I {} heroku config:set {}
else
    xargs -a ./.env/.env -I {} heroku config:set {}
    echo "===============================Initializing Database=================================="
    make init_db yml=docker-compose.yml || exit 9
    echo "===============================Inserting Sample Data=================================="
    make seed_db yml=docker-compose.yml || exit 10
fi

echo "===============================Releasing Application==================================."
heroku container:release web || exit 11

echo "===============================Test Endpoints==================================."
curl "https://$REPO_NAME.herokuapp.com/" || exit 12
curl "https://$REPO_NAME.herokuapp.com/v1/user" || exit 13

echo "Application deployed successfully! :)"

popd &> /dev/null || exit 80
