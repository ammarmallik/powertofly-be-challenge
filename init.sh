#!/bin/sh

if [ "$FLASK_ENV" = "development" ]
then
    echo "Creating the database tables..."
    python wsgi.py initialize
    python wsgi.py insert_user_data
    echo "Tables created"
fi

exec "$@"
