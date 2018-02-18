from django.template import Library


register = Library()


@register.filter(is_safe=False)
def has_perm(value, arg):
    return value.has_perm(arg)
