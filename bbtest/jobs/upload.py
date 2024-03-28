from django_rq import job
from django.utils.timezone import now
from tempfile import NamedTemporaryFile
from PIL import Image
from datetime import timedelta
from bbtest.models import Upload, Asset


@job("low")
def image_paragraph_processor(upload_uuid, asset_uuid):
    upload = Upload.objects.get(uuid=upload_uuid)
    asset = Asset.objects.get(uuid=asset_uuid)

    with NamedTemporaryFile() as upload_file:
        upload.download_to_file(upload_file)
        upload.delete()

        try:
            image = Image.open(upload_file)
            if image.mode == "RGBA":
                image.load()
                background = Image.new("RGB", image.size, (255, 255, 255))
                background.paste(image, mask=image.split()[3])
                image = background
            elif image.mode != "RGB":
                image = image.convert("RGB")
            image.thumbnail((1200, 1200))
            with NamedTemporaryFile() as asset_file:
                image.save(asset_file, "JPEG", quality=95)

                asset.asset_class = "ImageParagraphAsset"
                asset.meta_data = {}

                asset.asset_object().upload_from_file(asset_file, "image/jpeg")

        except OSError:
            asset.is_broken = True

    asset.expire_at = now() + timedelta(hours=1)
    asset.save()


@job("low")
def image_paragraph_destroyer(asset_uuid):
    try:
        Asset.objects.get(uuid=asset_uuid).delete()
    except Asset.DoesNotExist:
        pass
