from ..models import *
from django import template

register = template.Library()


@register.simple_tag
def get_host_post(num=5):
    return Post.objects.all().order_by('-modified_time').order_by('-view')[:num]


@register.simple_tag
def get_navigations():
    return Navigation.objects.all()
