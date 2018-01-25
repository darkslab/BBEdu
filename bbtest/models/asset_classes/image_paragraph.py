from .base import Asset


class ImageParagraphAsset(Asset):
    def upload_from_file(self, file, content_type):
        self.storage_bucket().blob("%s/file" % (
            self.asset().prefix(),
        )).upload_from_file(file, rewind=True, content_type=content_type)
