#############################################################################
#                                                                           #
#                       Copyright 2022 Ammar Akbar.                         #
#                           All Rights Reserved.                            #
#                                                                           #
#############################################################################
# Author: Ammar Akbar                                                       #
#                                                                           #
# Dockerfile for building docker image.                                     #
#############################################################################
FROM python:3.9.5-slim-buster as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends gcc

RUN pip install --upgrade pip
COPY . /usr/src/app/
RUN pip install flake8==4.0.1
RUN pip install isort==5.10.1
RUN flake8
RUN isort -c .

COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

FROM python:3.9.5-slim-buster
RUN mkdir -p /home/powertofly

RUN addgroup --system powertofly && adduser --system --group powertofly

ENV APP_HOME=/home/powertofly
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

COPY . $APP_HOME

RUN chown -R powertofly:powertofly $APP_HOME
USER powertofly

CMD gunicorn --log-file=- wsgi:APP
