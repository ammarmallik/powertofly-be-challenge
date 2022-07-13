#!/bin/bash

if [ $# -eq 0 ]; then
    echo 'Please pass the repository name on hub.docker.com.'
    exit 1
fi

IMAGE_NAME="powertofly-be-challenge_flask"
REPO_NAME=$1
## make docker_build image=$IMAGE_NAME || exit 2
## make docker_run image=$IMAGE_NAME || exit 3

docker login || exit 4
docker tag $IMAGE_NAME:latest ammarmallik/$REPO_NAME:latest || exit 5
docker push ammarmallik/$REPO_NAME:latest || exit 6
heroku login || exit 7
docker login --username=_ --passwor`d=$(heroku auth:token) registry.heroku.com || exit 8

heroku container:push web || exit 9
heroku container:release web || exit 10

curl "https://$REPO_NAME.herokuapp.com/"
