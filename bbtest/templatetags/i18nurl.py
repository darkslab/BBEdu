from django.template import Library
from django.urls import translate_url


register = Library()


@register.simple_tag(takes_context=True)
def current_url_for_lang(context, lang_code, *args, **kwargs):
    return translate_url(context["request"].path, lang_code)

@register.filter(is_safe=False)
def url_for_lang(value, arg):
    return translate_url(value, arg)
