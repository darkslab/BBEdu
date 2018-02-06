class RedirectView(View):
    permanent = False     # permanent redirect or not
    url = None            # url string to redirect, may contain %s, kwargs are passed from HTTP verb  [ OR use pattern_name below ]
    pattern_name = None   # string to reverse, args and kwargs are passed from HTTP verb              [ OR use url above ]
    query_string = False  # include the query string in redirect or not

    def get_redirect_url(self, *args, **kwargs):
        # Override redirect url if above attributes are not enough
        return "https://google.com/"


class TemplateView(TemplateResponseMixin, ContextMixin, View):
    template_name = None  # name of the template
    content_type = None   # content type of the HTTP response

    def get_context_data(self, **kwargs):
        # Optionally add to context, i.e.:
        #     kwargs["monkey"] = "shmonkey"
        return super().get_context_data(**kwargs)


class FormView(TemplateResponseMixin, FormMixin, View):
    template_name = None  # name of the template
    content_type = None   # content type of the HTTP response

    initial = {}        # initial data for form
    form_class = None   # form class
    success_url = None  # redirect URL if form is valid
    prefix = None       # prefix data

    def get_initial(self):
        # Override initial data if above attribute is not enough
        return {"monkey": "shmonkey"}

    def get_prefix(self):
        # Override form prefix if above attribute is not enough
        return "monkey"

    def get_form_class(self):
        # Override form class if above attribute is not enough
        return MonkeyForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Optionally add kwargs to form, i.e.:
        #     kwargs["instance"] = object
        return kwargs

    def get_success_url(self):
        # Override redirect url if above attribute is not enough
        return "https://google.com"

    def form_valid(self, form):
        # Optionally do something with a form, i.e.:
        #     form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # Optionally add to context, i.e.:
        #     kwargs["monkey"] = "shmonkey"
        return super().get_context_data(**kwargs)


    def get(self, request, *args, **kwargs):
        # Optionally do stuff here
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Optionally do stuff here
        return super().post(request, *args, **kwargs)
