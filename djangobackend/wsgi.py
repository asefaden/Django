"""
WSGI config for djangobackend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import importlib

try:
	django_wsgi = importlib.import_module('django.core.wsgi')
	get_wsgi_application = django_wsgi.get_wsgi_application
except Exception:  # pragma: no cover - fall back when Django isn't installed/resolvable
	# Provide a minimal WSGI application that returns an informative error
	def application(environ, start_response):
		start_response('500 Internal Server Error', [('Content-Type', 'text/plain')])
		msg = (
			'Django is not available in this environment.\n'
			'Install Django and ensure PYTHONPATH is configured, or run this project in a proper virtualenv.'
		)
		return [msg.encode('utf-8')]
else:
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangobackend.settings')
	application = get_wsgi_application()
