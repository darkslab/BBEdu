from django.template import Library
from django.urls import translate_url


register = Library()


@register.simple_tag(takes_context=True)
def change_lang(context, lang_code, *args, **kwargs):
    return translate_url(context["request"].path, lang_code)
