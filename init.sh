#!/bin/bash
set -e
set -o pipefail

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'password')" | python manage.py shell
echo "Success"
