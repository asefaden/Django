"""
ASGI config for djangobackend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import importlib

try:
    django_asgi = importlib.import_module('django.core.handlers.asgi')
    get_asgi_application = django_asgi.get_asgi_application
except Exception:
    # Provide a minimal ASGI application that returns an informative error
    async def application(scope, receive, send):
        if scope['type'] == 'http':
            await send({
                'type': 'http.response.start',
                'status': 500,
                'headers': [(b'content-type', b'text/plain')],
            })
            msg = 'Django is not available in this environment.'
            await send({'type': 'http.response.body', 'body': msg.encode('utf-8')})
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangobackend.settings')
    application = get_asgi_application()
