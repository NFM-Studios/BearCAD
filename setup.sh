#!/bin/bash

echo Running Migrations.
python3 manage.py migrate

echo creating a superuser.
python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'demo@demo.com', 'admin')"

echo creating staticinfo
python3 manage.py shell -c "from pages.models import StaticInfo; StaticInfo.objects.get_or_create(pk=1);"

echo Collecting static files
python3 manage.py collectstatic --noinput

