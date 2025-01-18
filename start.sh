#!/bin/bash

cleanup() {
    echo "Killing background processes..."
    kill $django_pid
    kill $ng_pid
    exit 0
}

trap cleanup SIGINT SIGTERM

cd ./web
python3 manage.py runserver &
django_pid=$!

cd ../web_frontend
npx ng serve &
ng_pid=$!

wait $django_pid
wait $ng_pid