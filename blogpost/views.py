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


class TagsFilterView(CategoryView):

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return  tag.post_set.all()


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
        self.this_pk = kwargs.get('pk')
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        self.object.increase_view()
        return response

    def get_object(self, queryset=None):
        post = super(PostDetailView, self).get_object(queryset=queryset)
        return post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        category = self.object.category

        post_list = Post.objects.filter(category=category).order_by('id').all()

        prev_post = None
        next_post = None
        post_count = len(post_list)

        post_index = 0
        for i in range(post_count):
            if post_list[i].pk == self.object.pk:
                post_index = i

        if not post_index == 0:
            prev_post = post_index - 1
        if not post_index == post_count - 1:
            next_post = post_index + 1

        # print(post_index, prev_post, next_post)

        if not prev_post == None:
            prev_post = post_list[prev_post]
        if not next_post == None:
            next_post = post_list[next_post]

        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update(
            {
                'form': form,
                'comment_list': comment_list,
                'next_post': next_post,
                'prev_post': prev_post,
            }
        )
        return context


class TagsView(ListView):
    model = Tag
    template_name = 'blog/tags.html'
    context_object_name = 'tags'
