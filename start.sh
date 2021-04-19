#!/bin/bash

# This relies on realpath being installed

REPO_PATH="$(dirname "$(dirname "$(realpath "$0")")")"

PYTHONPATH=:${REPO_PATH} FLASK_APP=${REPO_PATH}/app.py FLASK_DEBUG=1 python3 -m flask run --host=0.0.0.0 --port=8080 >> ./app.log 2>&1 &
