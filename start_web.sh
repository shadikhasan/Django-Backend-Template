#!/bin/bash
set -e

echo "🔄 Waiting for database to be ready..."
python manage.py wait_for_db

echo "📦 Making migrations..."
python manage.py makemigrations

echo "🚀 Running migrations..."
python manage.py migrate

echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

echo "🌐 Starting Django server..."
python manage.py runserver 0.0.0.0:8000
