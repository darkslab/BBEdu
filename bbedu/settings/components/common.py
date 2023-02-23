import os
from pathlib import Path
from json import load
from re import match
from bbedu.settings import BASE_DIR, BASE_DIR_PATH

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = Path(__file__).resolve().parent.parent.parent
# BASE_DIR_PATH = Path(BASE_DIR).resolve()
# print(BASE_DIR)
# print(BASE_DIR_PATH)

SECRETS = {}
VERSION = "dev"
version_match = match(r"^(?P<version>v\d+?\.\d+?\.\d+?)-[0-9a-f]{8}", BASE_DIR_PATH.name)
if version_match:
    VERSION = version_match.group("version")
try:
    with (BASE_DIR_PATH / "secrets.json").open() as settings_file:
        SECRETS = load(settings_file)
except (OSError, ValueError):
    pass

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRETS["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = SECRETS["DEBUG"]
STAGING = SECRETS["STAGING"]

ALLOWED_HOSTS = SECRETS["ALLOWED_HOSTS"]
LOGOUT_REDIRECT_URL = '/'
ROOT_URLCONF = 'bbedu.urls'
WSGI_APPLICATION = 'bbedu.wsgi.application'


# Application definition

INSTALLED_APPS = [
    "bbtest",
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "widget_tweaks",
    "pipeline",
    "django_rq",
    "captcha",
]

MIDDLEWARE = [
    "bbtest.middleware.turbolinks.RedirectHeaderMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "bbtest.template.context_processors.global_variables",
            ],
        },
    },
]