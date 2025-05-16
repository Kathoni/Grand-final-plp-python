from django import template

register = template.Library()

@register.filter
def dict_get(d, key):
    if isinstance(d, dict):
        return d.get(key, 0)
    return 0

@register.filter
def subtract(value, arg):
    # Both value and arg should be numbers
    try:
        return value - arg
    except Exception:
        return value  # fallback if arg is invalid
