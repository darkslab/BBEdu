LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[%(server_time)s] %(message)s",
        },
        "django.mysql": {
            "()": "bbtest.logging.MysqlFormatter",
            "format": "[%(server_time)s] %(message)s",
        },
    },
    "handlers": {
        "production_console": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "logging.StreamHandler",
        },
        "development_console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "django.server": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "django.server",
        },
        "django.mysql": {
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "django.mysql",
        },
    },
    "loggers": {
        "django": {
            "handlers": [
                "production_console",
                "development_console",
                "mail_admins",
            ],
            "level": "INFO",
        },
        "django.server": {
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["django.mysql"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}