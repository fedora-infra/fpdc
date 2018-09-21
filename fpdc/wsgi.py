"""
WSGI config for fpdc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# The prod.py file is used in production and maintained in ansible
# https://infrastructure.fedoraproject.org/cgit/ansible.git/tree/roles/openshift-apps/fpdc/templates/configmap.yml
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fpdc.settings.prod")

application = get_wsgi_application()
