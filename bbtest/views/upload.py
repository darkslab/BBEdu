from django.views.generic import View
from django.urls import reverse
from json import loads
from bbtest.auth.mixins import LoginRequiredMixin
from bbtest.forms.upload import UploadStartForm
from bbtest.http import TightJsonResponse


class UploadStartView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = UploadStartForm(data=request.POST)
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
        # DARK_TODO  implement this
        pass


class UploadAdoptView(LoginRequiredMixin, View):
    def post(self, request, uuid, *args, **kwargs):
        # DARK_TODO  implement this
        pass
