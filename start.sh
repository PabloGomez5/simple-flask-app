#!/bin/bash

echo "Starting" >> ./app.log

/usr/bin/gunicorn --bind 0.0.0.0:8080 wsgi:app -c gunicorn.conf.py &
