from datetime import timedelta

from django.db.models import Count, Q

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
def get_dailySentence():
    return DailySentence.objects.all().first()


@register.simple_tag
def get_broadcast():
    return Broadcast.objects.all()


# @register.simple_tag
# def get_host_week():
#     dt_s = datetime.datetime.now().date()
#     dt_e = (dt_s - timedelta(7))
#     post_list = Post.objects.filter(Q(modified_time=dt_s) & Q(modified_time=dt_e)).all().order_by(
#         '-modified_time').order_by('-view')[1:5]
#
#     return post_list
#
#
# @register.simple_tag
# def get_host_week_first():
#     dt_s = datetime.datetime.now().date()
#     dt_e = (dt_s - timedelta(7))
#     post = Post.objects.filter(Q(modified_time=dt_s) & Q(modified_time=dt_e)).all().order_by(
#         '-modified_time').order_by('-view').first()
#     return post
