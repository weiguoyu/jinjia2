#!/usr/bin/env bash

celery worker -A async_tasks -l info &

python app.py &

echo "server is running"

