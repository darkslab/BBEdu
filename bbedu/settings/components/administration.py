from bbedu.settings.components.common import SECRETS


ADMINS = [
    ("Darkhan Baimyrza", "darkhan@baimyrza.com"),
    ("Dmitriy Fedorov", "d.d.96@yandex.ru"),
]
EMAIL_SUBJECT_PREFIX = ""
DEFAULT_FROM_EMAIL = "bbtest.kz <no-reply@bbtest.kz>"
SERVER_EMAIL = "bbtest.kz ERROR <errors@bbtest.kz>"
if SECRETS["LOCAL_EMAIL_FORCED"]:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = SECRETS["LOCAL_EMAIL_HOST"]
    EMAIL_PORT = 1025
else:
    EMAIL_BACKEND = "bbtest.mail.backends.async.EmailBackend"
    AWS_ACCESS_KEY_ID = SECRETS["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY = SECRETS["AWS_SECRET_ACCESS_KEY"]
    AWS_REGION_NAME = SECRETS["AWS_REGION_NAME"]


BB_USER_AGENT = "bbtest.kz"

BB_MANAGERS = [
    "darkhan@bbtest.kz",
    "admin@bbtest.kz",
    "junior@bbtest.kz",
    "d.d.96@yandex.ru"
]

BB_BASE_URL = SECRETS["BASE_URL"]



FORMAT_MODULE_PATH = [
    "bbtest.formats",
]