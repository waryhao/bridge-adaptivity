#!/usr/bin/env bash

python manage.py migrate --settings=config.settings.prod
python manage.py collectstatic -v 3 -c --noinput --settings=config.settings.prod
sleep 5 && /usr/local/bin/gunicorn config.wsgi:application -w 2 -b :8000 --log-file=/dev/stdout --log-level=info --access-logfile=/dev/stdout
