from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import Http404
from json import loads
from bbtest.auth.mixins import LoginRequiredMixin
from bbtest.views.generic import View
from bbtest.forms.upload import UploadStartForm, UploadAdoptForm
from bbtest.http import TightJsonResponse
from bbtest.models import Upload, Asset
import bbtest.upload_processors
import bbtest.asset_adopters


class UploadStartView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = UploadStartForm("%s://%s" % (request.scheme, request.get_host()), data=request.POST)
        if not form.is_valid():
            return TightJsonResponse({
                "success": False,
                "errors": loads(form.errors.as_json()),
            }, status=400)

        upload = form.save()
        try:
            result = form.upload_starter_function()(upload, **form.upload_starter_kwargs())
            upload.upload_processor = result["upload_processor"]
            upload.save()
        except Exception:
            upload.delete()
            raise

        response = {}
        response.update(result.get("response", {}))
        response.update({
            "success": True,
            "upload_url": upload.upload_url,
            "complete_url": reverse("bbtest:upload_complete", kwargs={ "uuid": upload.uuid }),
        })
        return TightJsonResponse(response)


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
            result["job"].delay(upload.uuid, asset.uuid)
        except Exception:
            asset.delete()
            Upload.objects.filter(uuid=upload.uuid).update(expire_at=upload.expire_at)
            raise

        response = {
            "success": True,
        }
        if asset.asset_adopter:
            response["adopt_url"] = reverse("bbtest:upload_adopt", kwargs={ "uuid": asset.uuid }),
        return TightJsonResponse(response)


class UploadAdoptView(LoginRequiredMixin, View):
    def post(self, request, uuid, *args, **kwargs):
        form = UploadAdoptForm(data=request.POST)
        if not form.is_valid():
            return TightJsonResponse({
                "success": False,
                "broken": False,
                "errors": loads(form.errors.as_json()),
            }, status=400)

        asset = get_object_or_404(Asset.unadopted_objects, uuid=uuid)
        if not asset.is_ready_for_adoption():
            return TightJsonResponse({
                "success": False,
                "broken": False,
            })
        if not Asset.unadopted_objects.filter(uuid=uuid).update(asset_adopter=None, expire_at=None):
            raise Http404("Asset has already been adopted")

        if asset.is_broken:
            asset.delete()
            return TightJsonResponse({
                "success": False,
                "broken": True,
            })

        try:
            result = getattr(bbtest.asset_adopters, asset.asset_adopter)(asset, **form.cleaned_data["data"])
        except Exception:
            Asset.objects.filter(uuid=asset.uuid).update(asset_adopter=asset.asset_adopter, expire_at=asset.expire_at)
            raise

        result.update({
            "success": True,
            "broken": False,
        })
        return TightJsonResponse(result)
