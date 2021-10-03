"""
ASGI config for fig_cel project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import notify_app.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fig_cel.settings')
application = get_asgi_application()


application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            notify_app.routing.websocket_urlpatterns
        )
    ),
})