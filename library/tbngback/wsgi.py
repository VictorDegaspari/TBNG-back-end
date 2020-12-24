"""
WSGI config for tbngback project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/full/path/to/TBNG-back-end/library')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tbngback.settings')

application = get_wsgi_application()
