#!/usr/bin/env bash
# run the app with gunicorn
gunicorn shield_sql.wsgi:application --bind 0.0.0.0:${PORT:-10000}
