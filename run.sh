#!/bin/bash
set -e
set -o pipefail

source env/bin/activate
nohup python manage.py runserver 0.0.0.0:8000 &
