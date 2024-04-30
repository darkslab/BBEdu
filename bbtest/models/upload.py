from datetime import timedelta
from uuid import uuid4

from django.conf import settings
from django.db.models import (
    BigIntegerField,
    BooleanField,
    CharField,
    DateTimeField,
    Manager,
    Model,
    URLField,
)
from django.utils.timezone import now
from django.utils.translation import pgettext_lazy
from google.cloud.storage import Client
from google.oauth2.service_account import Credentials

from . import asset_classes
from .fields import JSONField


def storage_bucket():
    return Client(
        project=settings.SECRETS["GOOGLE_SERVICE_ACCOUNT_CREDENTIALS"].get("project_id"),
        credentials=Credentials.from_service_account_info(settings.SECRETS["GOOGLE_SERVICE_ACCOUNT_CREDENTIALS"]),
    ).bucket(settings.SECRETS["GOOGLE_STORAGE_BUCKET"])


def expiring_url(asset_object_name, expire_in=3600):
    url = storage_bucket().blob(asset_object_name).generate_signed_url(now() + timedelta(seconds=(expire_in + 5)))
    if not settings.DEBUG:
        ORIGINAL_API_ACCESS_ENDPOINT = "https://storage.googleapis.com"
        if url[:len(ORIGINAL_API_ACCESS_ENDPOINT)] == ORIGINAL_API_ACCESS_ENDPOINT:
            url = "%s%s" % (settings.SECRETS["GOOGLE_STORAGE_OVERRIDE_API_ACCESS_ENDPOINT"], url[len(ORIGINAL_API_ACCESS_ENDPOINT):])
    return url


class UploadingObjectsManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(expire_at__isnull=False)

class Upload(Model):
    uuid              = CharField        ( pgettext_lazy("Model field", "uuid"),              max_length=32,                                         primary_key=True, )
    expire_at         = DateTimeField    ( pgettext_lazy("Model field", "expire at"),                          null=True, blank=True, db_index=True,                   )
    upload_processor  = CharField        ( pgettext_lazy("Model field", "upload processor"),  max_length=100,  null=True, blank=True,                                  )
    upload_url        = URLField         ( pgettext_lazy("Model field", "upload URL"),        max_length=1000, null=True, blank=True,                                  )
    file_name         = CharField        ( pgettext_lazy("Model field", "file name"),         max_length=200,                                                          )
    file_size         = BigIntegerField  ( pgettext_lazy("Model field", "file size"),                                                                                  )
    file_type         = CharField        ( pgettext_lazy("Model field", "file content type"), max_length=200,             blank=True,                                  )

    objects = Manager()
    uploading_objects = UploadingObjectsManager()

    class Meta:
        default_permissions = ()

    def __str__(self):
        if not self.uuid:
            return "New Upload"
        return "Upload <%s>" % self.uuid

    def is_uploading(self):
        return self.expire_at is not None

    def is_uploaded(self):
        if not self.uuid:
            return False
        return self.__blob().exists()

    def generate_upload_url(self, origin):
        if not self.uuid or self.file_size is None:
            return None
        return self.__blob().create_resumable_upload_session(size=self.file_size, origin=origin)

    def download_to_file(self, file):
        self.__blob().download_to_file(file)

    def delete(self, **kwargs):
        blob = self.__blob()
        if blob:
            blob.delete()
        super().delete(**kwargs)

    def __blob(self):
        if not self.uuid:
            return None
        return storage_bucket().blob("uploads/%s" % self.uuid)


class AssetManager(Manager):
    def create(self, **kwargs):
        uuid = None
        while True:
            uuid = uuid4().hex
            if not self.model.objects.filter(uuid=uuid).exists():
                break
        kwargs.update({"uuid": uuid})
        return super().create(**kwargs)

class UnadoptedObjectsManager(AssetManager):
    def get_queryset(self):
        return super().get_queryset().filter(asset_adopter__isnull=False)

class Asset(Model):
    uuid           = CharField      ( pgettext_lazy("Model field", "uuid"),          max_length=32,                                                       primary_key=True, )
    expire_at      = DateTimeField  ( pgettext_lazy("Model field", "expire at"),                     null=True, blank=True, db_index=True,                                  )
    asset_adopter  = CharField      ( pgettext_lazy("Model field", "asset adopter"), max_length=100, null=True, blank=True,                                                 )
    is_broken      = BooleanField   ( pgettext_lazy("Model field", "broken?"),                                                             default=False,                   )
    asset_class    = CharField      ( pgettext_lazy("Model field", "asset class"),   max_length=100, null=True, blank=True,                                                 )
    meta_data      = JSONField      ( pgettext_lazy("Model field", "meta data"),                     null=True, blank=True,                                                 )

    objects = AssetManager()
    unadopted_objects = UnadoptedObjectsManager()

    class Meta:
        default_permissions = ()

    def __str__(self):
        if not self.uuid:
            return "New Asset"
        return "Asset <%s>" % self.uuid

    def is_ready_for_adoption(self):
        return self.asset_adopter is not None and self.expire_at is not None

    def is_adopted(self):
        return not self.is_broken and self.asset_adopter is None and self.expire_at is None

    def prefix(self):
        if not self.uuid:
            return None
        return "assets/%s" % self.uuid

    def asset_object(self):
        if self.asset_class is None or self.meta_data is None:
            return None
        return getattr(asset_classes, self.asset_class)(self, storage_bucket(), **self.meta_data)

    def delete(self, **kwargs):
        asset_object = self.asset_object()
        if asset_object:
            asset_object.delete()
        super().delete(**kwargs)
