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


class Friendly(models.Model):
    title = models.CharField(max_length=128, verbose_name='网站名称')
    weburl = models.URLField(max_length=128, verbose_name='网站URL')
    email = models.EmailField(max_length=128, verbose_name='联系邮箱')
    desc = models.TextField(verbose_name='网站说明')
    reason = models.TextField(verbose_name='理由')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_time = models.DateTimeField(blank=True, verbose_name='变更时间')
    flag = models.BooleanField(default=False, verbose_name='验证')

    class Meta:
        ordering = ['-created_time']
        verbose_name = u"友情链接"
        verbose_name_plural = u"友情链接"
