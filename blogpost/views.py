from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from blogpost.models import *
from comments.forms import CommentForm


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        self.object.increase_view()
        return response

    def get_object(self, queryset=None):
        post = super(PostDetailView, self).get_object(queryset=queryset)
        return post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update(
            {
                'form': form,
                'comment_list': comment_list,
            }
        )
        return context
