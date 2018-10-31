from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from blogpost.models import *


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        post = super(PostDetailView, self).get_object(queryset=queryset)
        return post
