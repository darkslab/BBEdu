from django.conf import settings


class RedirectHeaderMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response
        self._cookie_name = "turbolinks"

    def __call__(self, request):
        turbolinks_location = request.COOKIES.get(self._cookie_name)

        response = self._get_response(request)

        if response.status_code in (301, 302):
            location = "/"
            try:
                if len(response["Location"]) <= 1000:
                    location = response["Location"]
            except KeyError:
                pass
            response.set_cookie(
                self._cookie_name,
                location,
                domain=settings.SESSION_COOKIE_DOMAIN,
                secure=settings.SESSION_COOKIE_SECURE or None,
                httponly=settings.SESSION_COOKIE_HTTPONLY or None,
            )
        elif turbolinks_location:
            response["Turbolinks-Location"] = turbolinks_location
            response.delete_cookie(
                self._cookie_name,
                domain=settings.SESSION_COOKIE_DOMAIN,
            )
        return response
