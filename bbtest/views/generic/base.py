from django.views.generic.base import TemplateResponseMixin, ContextMixin, View
from django.views.generic.edit import FormMixin


class TemplateView(TemplateResponseMixin, ContextMixin, View):
    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())


class FormView(TemplateResponseMixin, FormMixin, View):
    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
