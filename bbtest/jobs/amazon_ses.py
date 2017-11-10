from django_rq import job
from django.conf import settings
from django.utils.timezone import now
from bbtest.models import Email
import boto3


@job("low")
def send_email(email_id):
    email = Email.objects.get(pk=email_id)
    client = boto3.client(
        "ses",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION_NAME,
    )
    client.send_raw_email(RawMessage={
        "Data": email.mime_data,
    })
    email.sent_at = now()
    email.save()
