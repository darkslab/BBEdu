class RedirectView(View):
    permanent = False     # permanent redirect or not
    url = None            # url string to redirect, may contain %s, kwargs are passed from HTTP verb  [ OR use pattern_name below ]
    pattern_name = None   # string to reverse, args and kwargs are passed from HTTP verb              [ OR use url above ]
    query_string = False  # include the query string in redirect or not

    def get_redirect_url(self, *args, **kwargs):
        # Override redirect url if above attributes are not enough
        pass

    def get(self, request, *args, **kwargs): pass
    def head(self, request, *args, **kwargs): pass
    def post(self, request, *args, **kwargs): pass
    def options(self, request, *args, **kwargs): pass
    def delete(self, request, *args, **kwargs): pass
    def put(self, request, *args, **kwargs): pass
    def patch(self, request, *args, **kwargs): pass


class TemplateView(TemplateResponseMixin, ContextMixin, View):
    template_name = None  # name of the template
    content_type = None   # content type of the HTTP response

    def get_context_data(self, **kwargs):
        # Pass some extra context data to kwargs
        pass

    def get(self, request, *args, **kwargs): pass
    def head(self, request, *args, **kwargs): pass


class FormView(TemplateResponseMixin, BaseFormView):
    template_name = None  # name of the template
    content_type = None   # content type of the HTTP response

    initial = {}        # initial data for form
    form_class = None   # form class
    success_url = None  # redirect URL if form is valid

    def get_context_data(self, **kwargs):
        # Pass some extra context data to kwargs
        pass

    def form_valid(self, form):
        # Do something with form before success redirection
        pass

    def get(self, request, *args, **kwargs): pass
    def head(self, request, *args, **kwargs): pass
    def post(self, request, *args, **kwargs): pass
    def put(self, request, *args, **kwargs): pass


class DetailView(SingleObjectTemplateResponseMixin, BaseDetailView):
    template_name = None  # name of the template
    content_type = None   # content type of the HTTP response

    pk_url_kwarg = 'pk'

    def get_queryset(self):
        # OVERRIDE THIS!
        pass

    def get_context_data(self, **kwargs):
        # Pass some extra context data to kwargs
        # self.object is useful here
        pass

    def get(self, request, *args, **kwargs): pass
    def head(self, request, *args, **kwargs): pass


class DetailFormView(SingleObjectTemplateResponseMixin, FormMixin, SingleObjectMixin, ProcessFormView):
    template_name = None  # name of the template
    content_type = None   # content type of the HTTP response

    initial = {}        # initial data for form
    form_class = None   # form class
    success_url = None  # redirect URL if form is valid

    pk_url_kwarg = 'pk'

    def get_queryset(self):
        # OVERRIDE THIS!
        pass

    def get_context_data(self, **kwargs):
        # Pass some extra context data to kwargs
        # self.object is useful here
        pass

    def form_valid(self, form):
        # Do something with form before success redirection
        # self.object is useful here
        pass

    def get(self, request, *args, **kwargs): pass
    def head(self, request, *args, **kwargs): pass
    def post(self, request, *args, **kwargs): pass
    def put(self, request, *args, **kwargs): pass
