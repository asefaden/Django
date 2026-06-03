#!/bin/bash
gunicorn djangobackend.wsgi:application --bind 0.0.0.0:8000
