from django.conf import settings


def global_variables(request):
    context = {}
    context["VERSION"] = None
    if settings.VERSION != "dev" or settings.DEBUG:
        context["VERSION"] = settings.VERSION
    context["ANALYTICS"] = not settings.DEBUG and not settings.STAGING
    context["BASE_URL"] = settings.BB_BASE_URL
    context["LANGUAGE_CODE_KK"] = settings.BB_LANGUAGE_CODE_KK
    context["LANGUAGE_CODE_RU"] = settings.BB_LANGUAGE_CODE_RU
    context["LANGUAGE_CODE_EN"] = settings.BB_LANGUAGE_CODE_EN
    return context
