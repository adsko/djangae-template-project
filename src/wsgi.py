import sys
import os
from os.path import dirname, abspath, join, exists

PROJECT_DIR = dirname(abspath(__file__))
SITEPACKAGES_DIR = join(PROJECT_DIR, "sitepackages")

if SITEPACKAGES_DIR not in sys.path:
    sys.path.insert(1, SITEPACKAGES_DIR)

from django.core.wsgi import get_wsgi_application
from djangae.wsgi import DjangaeApplication
from djangae.environment import is_production_environment

settings = "settings_live" if is_production_environment() else "settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)
application = DjangaeApplication(get_wsgi_application())
