from django.core.mail import mail_admins
from io import StringIO
from traceback import print_tb


def exception(job, exc_type, exc_value, traceback):
    if job.func_name == "bbtest.jobs.amazon_ses.send_email":
        return
    str_buffer = StringIO()
    print_tb(traceback, file=str_buffer)
    subject = "WORKER ERROR: %s" % job.description
    message = "%s: %s\n\n%s" % (
        exc_type.__name__,
        str(exc_value),
        str_buffer.getvalue(),
    )
    mail_admins(subject, message)
