# Powertofly-BE-Challenge
This repository contains a Dockerized Flask project that includes an API to retrieve users from the database with pagination, filtration and simple caching support.


#### Pre-requisites:

- Python3.8
- Docker version 20.10.12, build 20.10.12-0ubuntu2~20.04.1
- Docker Compose version v2.6.1
- GNU Make 4.2.1
- heroku/7.60.2 linux-x64 node-v14.19.0
- psql (PostgreSQL) 12.11 (Ubuntu 12.11-0ubuntu0.20.04.1)
- gunicorn (version 20.1.0)

#### Set .env:

- Create `powertofly-be-challenge/.env` directory and add the following files:
    1. .env
        ```
         FLASK_APP=api/__init__.py
         FLASK_ENV=development
         POSTGRES_USER=powertofly
         POSTGRES_PASSWORD=powertofly
         POSTGRES_DB=powertofly_dev
         POSTGRES_HOST=postgres
         POSTGRES_PORT=5432
    2. .env.db
        ```
         POSTGRES_USER=powertofly
         POSTGRES_PASSWORD=powertofly
         POSTGRES_DB=powertofly_dev

Note: These environment variables should be set according to the production so change them while production deployment.

#### Database setup:

- Create DB: `powertofly_dev`
- Create User: `powertofly`
- Grant privileges on DB to User.

#### Run locally:


    make build_and_run yml=docker-compose.yml
    make logs yml=docker-compose.yml
    curl http://127.0.0.1:5000/
    
This should print `OK` if ran successfully.

#### Deployment command:

`./deploy.sh <docker-username> <docker-repository> <environment>`

#### Supported Environments:

- development
- production

## APIs:

### 1. Health API:
This API is to check the health of the Flask application.

##### URL: `http(s)://<IP-ADDRESS>:<PORT>/`
##### Endpoint: `/`
##### Method: `GET`
##### Response: `OK`
##### cURL: `curl --location --request GET 'http(s)://<IP-ADDRESS>:<PORT>/'`

### 2. Fetch Users API:
This API fetches the users from the database using the filtration, pagination and caches them accordingly. 

It implements:

- Pagination
- Filtration
- Caching
- Template rendering for showing users.

##### URL: `http(s)://<IP-ADDRESS>:<PORT>/v1/user`
##### Endpoint: `/v1/user`
##### Method: `GET | POST`
##### Params:

- <b>page:</b> Page number. By default it is `1`. (integer)
- <b>per_page:</b> Rows per page. By default it is `50`. (integer)
- <b>filter:</b> Search string from User table. Only checks in email & country columns and filters records. Default value is empty string. (string)
- <b>format:</b> Output format e.g. json/html. By default it is `json`. (integer)

##### Query params: `?page=1&per_page=50&filter=Pakistan&format=json`
##### Form Data: `filter: <search-string>`
##### JSON Response:

    {
        "curr_page":1,
        "prev_page":null,
        "next_page":2,
        "total_pages":500000,
        "data": [
            {
                 "id":1,
                 "name":"User 1",
                 "email":"user_1@powertofly.com",
                 "country":"Isle of Man",
                 "created_at":"Thu, 14 Jul 2022 21:10:27 GMT"
            },
            {
                 "id":2,
                 "name":"User 2",
                 "email":"user_2@powertofly.com",
                 "country":"American Samoa",
                 "created_at":"Thu, 14 Jul 2022 21:10:27 GMT"
            }
        ]
    }

##### HTML Response:

![powertofly-html-resp](https://user-images.githubusercontent.com/29196434/179128872-59b4aa9b-b77b-4caf-8ea5-cf21a5f2fd8a.png)

##### cURL GET: `curl --location --request GET 'https://powertofly-flask-api.herokuapp.com/v1/user?page=2&per_page=2&format=html&filter=Pakistan'`
##### cURL POST: `curl --location --request POST 'https://powertofly-flask-api.herokuapp.com/v1/user?page=2&per_page=2&format=html'--form 'filter="Pakistan"'`


## Heroku APIs:

#### User API: `https://powertofly-flask-api.herokuapp.com/v1/user?page=2&per_page=2&format=html&filter=Pakistan`
#### Health API: `https://powertofly-flask-api.herokuapp.com/`
