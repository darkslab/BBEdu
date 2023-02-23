import os
from bbedu.settings.components.common import SECRETS

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        "HOST": os.environ['DATABASES_DEFAULT_HOST'],  #SECRETS["DATABASES_DEFAULT_HOST"],
        "PORT": 3306,
        "NAME": os.environ['DATABASES_DEFAULT_NAME'],  # SECRETS["DATABASES_DEFAULT_NAME"],
        "USER": os.environ['DATABASES_DEFAULT_USER'],  # SECRETS["DATABASES_DEFAULT_USER"],
        "PASSWORD": os.environ['DATABASES_DEFAULT_PASSWORD'],  # SECRETS["DATABASES_DEFAULT_PASSWORD"],
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


RQ_QUEUES = {
    "default": {
        "HOST": SECRETS["BROKER_HOST"],
        "PORT": 6379,
        "DB": 0,
        "PASSWORD": SECRETS["BROKER_PASSWORD"],
        "DEFAULT_TIMEOUT": 300,
    },
}
RQ_QUEUES["high"] = RQ_QUEUES["default"]
RQ_QUEUES["low"] = RQ_QUEUES["default"]
RQ_EXCEPTION_HANDLERS = [
    "bbtest.rq.handlers.exception",
    "rq.handlers.move_to_failed_queue",
]


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": os.environ['CACHES_DEFAULT_LOCATION'], # SECRETS["CACHES_DEFAULT_LOCATION"],
    }
}