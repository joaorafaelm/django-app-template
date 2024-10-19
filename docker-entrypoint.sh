#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# run honcho
echo "Run honcho"
honcho start

exec "$@"
