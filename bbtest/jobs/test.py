from django_rq import job


@job("high")
def test():
    raise NotImplementedError("Please implement test function")
