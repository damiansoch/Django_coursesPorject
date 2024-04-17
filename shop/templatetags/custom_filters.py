from django import template

register = template.Library()


@register.filter(name="split_first")
def split_first(value, delimiter=" "):
    parts = value.split(delimiter)
    return parts[0] if parts else value
