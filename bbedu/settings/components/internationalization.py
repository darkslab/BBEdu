from bbedu.settings.components.common  import BASE_DIR_PATH

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

BB_LANGUAGE_CODE_KK = "kk"
BB_LANGUAGE_CODE_RU = "ru"
BB_LANGUAGE_CODE_EN = "en"

LANGUAGE_CODE = BB_LANGUAGE_CODE_RU
LANGUAGES = [
    (BB_LANGUAGE_CODE_KK, "Kazakh"),
    (BB_LANGUAGE_CODE_RU, "Russian"),
    (BB_LANGUAGE_CODE_EN, "English"),
]
LOCALE_PATHS = [
    str(BASE_DIR_PATH / "i18n"),
]

TIME_ZONE = "Asia/Almaty"

USE_I18N = True
USE_L10N = True
USE_TZ = True
USE_DEPRECATED_PYTZ = True