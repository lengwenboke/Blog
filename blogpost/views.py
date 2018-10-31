from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from blogpost.models import *


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

