from django_rq import job


@job("high")
def test():
    return True
