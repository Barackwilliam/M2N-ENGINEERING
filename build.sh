#!/usr/bin/env bash
# Build script kwa Render — inafanya kazi moja kwa moja wakati wa deployment

set -o errexit  # Simama kama command ikifail

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
