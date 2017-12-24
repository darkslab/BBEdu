from django.http import JsonResponse


class TightJsonResponse(JsonResponse):
    def __init__(self, data, *args, **kwargs):
        _kwargs = {}
        if len(args) < 3:
            _kwargs.update({
                "json_dumps_params": {
                    "separators": (",", ":"),
                },
            })
        _kwargs.update(kwargs)
        super().__init__(data, *args, **_kwargs)
