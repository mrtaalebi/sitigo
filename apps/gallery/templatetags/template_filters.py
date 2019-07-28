from django import template

register = template.Library()

@register.filter
def modulo(a, b):
    return a % b

