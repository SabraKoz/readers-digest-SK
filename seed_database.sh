#!/bin/bash

rm db.sqlite3
rm -rf ./digestapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations digestapi
python3 manage.py migrate digestapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata categories
python3 manage.py loaddata books
python3 manage.py loaddata reviews

