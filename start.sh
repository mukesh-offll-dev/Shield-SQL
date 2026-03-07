#!/usr/bin/env bash
# run the app with gunicorn
gunicorn shield_sql.wsgi:application
