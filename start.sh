#!/bin/zsh

cd ./web
python3 manage.py runserver &
cd ../web_frontend
ng serve