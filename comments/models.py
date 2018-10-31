from django.db import models

# Create your models here.
from blogpost.models import Post


class Comment(models.Model):
    """
    评论
    """
    name = models.CharField(max_length=32, verbose_name="昵称")
    email = models.EmailField(max_length=64, verbose_name="邮箱")
    text = models.TextField(verbose_name="评论内容")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")

    author_reply = models.TextField(blank=True, verbose_name="作者回复")

    post = models.ForeignKey(Post, verbose_name="文章")

    class Meta:
        ordering = ['-created_time']
        verbose_name = u"评论"
        verbose_name_plural = u"评论"


class Lmsg(models.Model):
    name = models.CharField(max_length=32, verbose_name="昵称")
    email = models.EmailField(max_length=64, verbose_name="邮箱")
    text = models.TextField(verbose_name="留言内容")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")

    class Meta:
        ordering = ['-created_time']
        verbose_name = u"留言"
        verbose_name_plural = u"留言"
