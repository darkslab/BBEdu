from django.template import Library


register = Library()


@register.simple_tag(takes_context=True)
def pagination_qs(context, page, *args, **kwargs):
    query = context.request.GET.copy()
    query["page"] = page
    return query.urlencode()
