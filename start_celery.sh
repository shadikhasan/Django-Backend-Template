#!/bin/bash
set -e

: "${CELERY_POOL:=solo}"
: "${CELERY_CONCURRENCY:=1}"
: "${CELERY_LOGLEVEL:=warning}"
: "${CELERY_WORKER_FLAGS:=--without-mingle --without-gossip}"

echo "🔄 Waiting for database..."
python manage.py wait_for_db

echo "🚀 Running migrations..."
python manage.py migrate --noinput


echo "🔁 Starting Celery worker..."
celery -A core worker \
  --loglevel="$CELERY_LOGLEVEL" \
  --pool="$CELERY_POOL" \
  --concurrency="$CELERY_CONCURRENCY" \
  $CELERY_WORKER_FLAGS &

echo "⏱️ Starting Celery beat..."
exec celery -A core beat --loglevel="$CELERY_LOGLEVEL"