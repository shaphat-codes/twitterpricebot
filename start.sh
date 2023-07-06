#!/bin/bash

python manage.py runserver 0.0.0.0:8000 & celery -A djangorediscelery beat -l INFO && fg