from django.conf import settings


def global_variables(request):
    return {
        "VERSION": settings.VERSION,
        "ANALYTICS": not settings.DEBUG,
    }
