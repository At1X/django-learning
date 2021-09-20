import datetime
from django import template

register = template.Library()

@register.simple_tag
def time():
    return datetime.datetime.now()
    