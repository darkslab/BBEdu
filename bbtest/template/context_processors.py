from django.conf import settings


def global_variables(request):
    context = {}
    context["VERSION"] = None
    if settings.VERSION != "dev" or settings.DEBUG:
        context["VERSION"] = settings.VERSION
    context["ANALYTICS"] = not settings.DEBUG and not settings.STAGING
    context["BASE_URL"] = settings.BB_BASE_URL
    return context
