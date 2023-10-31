#Entry point for the web server, when we deploy the project to live server 

"""
ASGI config for merkatoo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'merkatoo.settings')

application = get_asgi_application()
