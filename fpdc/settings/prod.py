import os
import json
from .base import *

# Directory where the configmap is monted in openshift
CONFIG_DIR = os.environ.get("OPENSHIFT_CONFIG_DIR", BASE_DIR)
DEBUG = False

ALLOWED_HOSTS = [os.environ.get("OPENSHIFT_APP_DNS")]

with open(os.path.join(CONFIG_DIR, "config.json")) as fp:
    data = json.load(fp)

SECRET_KEY = data["SECRET_KEY"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "fpdc",
        "USER": "fpdc",
        "PASSWORD": data["DB_PASSWORD"],
        "HOST": data["DB_HOST"],
        "PORT": "",
    }
}
