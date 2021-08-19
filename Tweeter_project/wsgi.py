"""
WSGI config for Tweeter_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

#aici se va face comunicarea dintre aplicatia web python si web serverul

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tweeter_project.settings')

application = get_wsgi_application()
