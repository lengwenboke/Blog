from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView

from blogpost.models import *
from comments.forms import CommentForm


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'


class CategoryView(IndexView):
    template_name = 'blog/list.html'

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


class NavigationView(CategoryView):
    model = Navigation
    context_object_name = 'navigation'

    def get_queryset(self):
        return super(NavigationView, self).get_queryset().filter(pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super(NavigationView, self).get_context_data(**kwargs)
        cates = self.object_list.first().category_set.all()
        post_list = []
        for cate in cates:
            posts = cate.post_set.all()
            for post in posts:
                post_list.append(post)
        context.update(
            {
                'post_list': post_list
            }
        )
        return context



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
