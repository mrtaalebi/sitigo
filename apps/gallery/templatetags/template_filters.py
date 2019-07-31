from django import template

register = template.Library()

@register.filter
def modulo(a, b):
    return a % b

@register.filter
def len(a):
    return len(a)
