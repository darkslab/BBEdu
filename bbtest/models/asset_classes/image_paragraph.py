from .base import Asset


class ImageParagraphAsset(Asset):
    def upload_from_file(self, file, content_type):
        self.storage_bucket().blob(self.object_name()).upload_from_file(file, rewind=True, content_type=content_type)

    def object_name(self):
        return "%s/file" % self.asset().prefix()

    def delete(self):
        self.storage_bucket().blob(self.object_name()).delete()
