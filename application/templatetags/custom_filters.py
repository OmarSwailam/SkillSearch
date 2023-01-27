from django import template

register = template.Library()

@register.filter()
def s(value):
    return len(value)