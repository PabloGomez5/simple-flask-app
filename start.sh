#!/bin/bash

echo "Starting" >> ./app.log

gunicorn --bind 0.0.0.0:8080 wsgi:app -c gunicorn.conf.py &
