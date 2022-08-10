#!/bin/bash
APP_PORT=${PORT:-8000}
cd /app/

# run production server using gunicorn
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm proc_sys.wsgi:application --bind "0.0.0.0:${APP_PORT}"