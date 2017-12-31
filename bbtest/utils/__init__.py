def remote_ip(request):
    proxy_ip = request.META.get("HTTP_X_FORWARDED_FOR")
    if proxy_ip is None:
        return request.META.get("REMOTE_ADDR")
    return proxy_ip.split(",")[0]
