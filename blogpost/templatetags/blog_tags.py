from django.db.models import Count

from comments.models import Comment
from ..models import *
from django import template

register = template.Library()


@register.simple_tag
def get_host_post(num=5):
    return Post.objects.all().order_by('-modified_time').order_by('-view')[:num]


@register.simple_tag
def get_navigations():
    return Navigation.objects.all()


@register.simple_tag
def get_recent_comment(num=5):
    return Comment.objects.all()[:num]


@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts_gt=0)
