FROM python:3.9.5-slim-buster as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends gcc

RUN pip install --upgrade pip
COPY . /usr/src/app/

COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

FROM python:3.9.5-slim-buster
RUN mkdir -p /home/powertofly

RUN addgroup --system powertofly && adduser --system --group powertofly

ENV HOME=/home
ENV APP_HOME=/home/powertofly
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y --no-install-recommends netcat
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

COPY ./init.sh $APP_HOME
COPY . $APP_HOME

RUN chown -R powertofly:powertofly $APP_HOME
USER powertofly
ENTRYPOINT ["/home/powertofly/init.sh"]

CMD gunicorn --log-file=- wsgi:APP
