from json import dumps


def tight_dumps(obj, *args, **kwargs):
    _kwargs = {}
    if len(args) < 7:
        _kwargs.update({
            "separators": (",", ":"),
        })
    _kwargs.update(kwargs)
    return dumps(obj, *args, **_kwargs)
