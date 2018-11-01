from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from blogpost.models import Post
from comments.forms import CommentForm, LsmgForm, Lmsg, FriendlyForm
from comments.models import Friendly


def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {
                'post': post,
                "form": form,
                "comment_list": comment_list
            }
            return render(request, 'blog/detail.html', context=context)
    return redirect(post)


def friendly_url(request):
    form = FriendlyForm()
    if request.method == 'POST':
        form = FriendlyForm(request.POST)
        if form.is_valid():
            friendly = form.save(commit=False)
            friendly.save()
            return redirect('comments:friendly')
    friendly_list = Friendly.objects.all()
    context = {
        'form': form,
        'friendly_list': friendly_list,
    }
    return render(request, 'blog/friendly.html', context=context)


def reader_lmsg(request):
    # print(request)
    form = LsmgForm()
    if request.method == 'POST':
        form = LsmgForm(request.POST)
        if form.is_valid():
            lmsg = form.save(commit=False)
            lmsg.save()
            return redirect('comments:lmsg')
    lmsg_list = Lmsg.objects.all()
    context = {
        'form': form,
        'lmsg_list': lmsg_list
    }
    return render(request, 'blog/lmsg.html', context=context)

    # return redirect('comments:lmsg')
