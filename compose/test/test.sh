#!/bin/sh

echo "Creating migrations and insert into psql database"
python3 manage.py makemigrations
python3 manage.py migrate

echo "Run the tests"
coverage run --source="." manage.py test **/api/tests/
