"""
WSGI config for eqg project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
https://docs.bitnami.com/aws/infrastructure/django/get-started/deploy-django-project/
"""

#APPROACH B
import os
import sys
sys.path.append('/opt/bitnami/projects/eqg')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/projects/eqg/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eqg.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
