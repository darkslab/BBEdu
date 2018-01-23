from django.db.models import Model, CharField, DateTimeField, BigIntegerField, BooleanField, URLField
from django.utils.translation import pgettext_lazy
from django.conf import settings
from google.oauth2.service_account import Credentials
from google.cloud.storage import Client
from .fields import JSONField


class Upload(Model):
    uuid              = CharField        ( pgettext_lazy("Model field", "uuid"),              max_length=32,                                         primary_key=True, )
    expire_at         = DateTimeField    ( pgettext_lazy("Model field", "expire at"),                          null=True, blank=True, db_index=True,                   )
    upload_processor  = CharField        ( pgettext_lazy("Model field", "upload processor"),  max_length=100,  null=True, blank=True,                                  )
    upload_url        = URLField         ( pgettext_lazy("Model field", "upload URL"),        max_length=1000, null=True, blank=True,                                  )
    file_name         = CharField        ( pgettext_lazy("Model field", "file name"),         max_length=200,                                                          )
    file_size         = BigIntegerField  ( pgettext_lazy("Model field", "file size"),                                                                                  )
    file_type         = CharField        ( pgettext_lazy("Model field", "file content type"), max_length=200,             blank=True,                                  )

    class Meta:
        default_permissions = ()

    def __str__(self):
        if not self.uuid:
            return "New Upload"
        return "Upload <%s>" % self.uuid

    def is_uploading(self):
        return self.expire_at is not None

    def generate_upload_url(self):
        if not self.uuid or not self.file_size:
            return None
        storage_client = Client(
            project=settings.SECRETS["GOOGLE_SERVICE_ACCOUNT_CREDENTIALS"].get("project_id"),
            credentials=Credentials.from_service_account_info(settings.SECRETS["GOOGLE_SERVICE_ACCOUNT_CREDENTIALS"]),
        )
        storage_object = storage_client.bucket(settings.SECRETS["GOOGLE_STORAGE_BUCKET"]).blob("uploads/%s" % self.uuid)
        return storage_object.create_resumable_upload_session(size=self.file_size)


class Asset(Model):
    uuid          = CharField      ( pgettext_lazy("Model field", "uuid"),         max_length=32,                                                       primary_key=True, )
    expire_at     = DateTimeField  ( pgettext_lazy("Model field", "expire at"),                    null=True, blank=True, db_index=True,                                  )
    file_adopter  = CharField      ( pgettext_lazy("Model field", "file adopter"), max_length=100, null=True, blank=True,                                                 )
    is_broken     = BooleanField   ( pgettext_lazy("Model field", "broken?"),                                                            default=False,                   )
    file_class    = CharField      ( pgettext_lazy("Model field", "file class"),   max_length=100, null=True, blank=True,                                                 )
    meta_data     = JSONField      ( pgettext_lazy("Model field", "meta data"),                    null=True, blank=True,                                                 )

    class Meta:
        default_permissions = ()

    def __str__(self):
        if not self.uuid:
            return "New Asset"
        return "Asset <%s>" % self.uuid
