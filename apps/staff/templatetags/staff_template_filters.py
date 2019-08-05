from django import template

register = template.Library()


@register.filter
def len(a):
    return a.__len__()


@register.filter
def modulo(a, b):
    return a % b


@register.filter
def name(staff, lang):
    if lang == "fa":
        return staff.persian_firstname + " " + staff.persian_lastname
    else:
        return staff.english_firstname + " " + staff.english_lastname

