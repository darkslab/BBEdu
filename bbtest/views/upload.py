from django.views.generic import View
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import Http404
from json import loads
from bbtest.auth.mixins import LoginRequiredMixin
from bbtest.forms.upload import UploadStartForm
from bbtest.http import TightJsonResponse
from bbtest.models import Upload, Asset
import bbtest.upload_processors


class UploadStartView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = UploadStartForm("%s://%s" % (request.scheme, request.get_host()), data=request.POST)
        if form.is_valid():
            upload = form.save()
            try:
                result = form.upload_starter_function()(upload, **form.upload_starter_kwargs())
                upload.upload_processor = result["upload_processor"]
                upload.save()
            except Exception:
                upload.delete()
                raise
            result["response"].update({
                "success": True,
                "upload_url": upload.upload_url,
                "complete_url": reverse("bbtest:upload_complete", kwargs={ "uuid": upload.uuid }),
            })
            return TightJsonResponse(result["response"])

        return TightJsonResponse({
            "success": False,
            "errors": loads(form.errors.as_json()),
        }, status=400)


class UploadCompleteView(LoginRequiredMixin, View):
    def post(self, request, uuid, *args, **kwargs):
        upload = get_object_or_404(Upload.uploading_objects, uuid=uuid)
        if not upload.is_uploaded():
            return TightJsonResponse({"success": False})
        if not Upload.uploading_objects.filter(uuid=upload.uuid).update(expire_at=None):
            raise Http404("Upload has already been completed")

        asset = Asset.objects.create()
        try:
            result = getattr(bbtest.upload_processors, upload.upload_processor)(upload, asset)
            asset.asset_adopter = result.get("asset_adopter", None)
            asset.save()
        except Exception:
            asset.delete()
            Upload.uploading_objects.filter(uuid=upload.uuid).update(expire_at=upload.expire_at)
            raise
        result["job"].delay(upload.uuid, asset.uuid)

        response = {
            "success": True,
        }
        if asset.asset_adopter:
            response["adopt_url"] = reverse("bbtest:upload_adopt", kwargs={ "uuid": asset.uuid }),
        return TightJsonResponse(response)


class UploadAdoptView(LoginRequiredMixin, View):
    def post(self, request, uuid, *args, **kwargs):
        # DARK_TODO  implement this
        pass
