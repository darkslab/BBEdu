

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "bbtest.auth.password_validation.MinLengthPasswordValidator",
    },
    {
        "NAME": "bbtest.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "bbtest.auth.password_validation.CommonPasswordValidator",
    },
]


AUTH_USER_MODEL = "bbtest.User"
AUTHENTICATION_BACKENDS = [
    "bbtest.auth.backends.Backend",
]
BB_REDIRECT_FIELDNAME = "r"