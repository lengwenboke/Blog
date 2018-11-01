import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.html import strip_tags
from mdeditor.fields import MDTextField


class Navigation(models.Model):
    """
    导航栏
    """
    # 导航栏名称
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"导航"
        verbose_name_plural = u"导航"


class Category(models.Model):
    """
    分类(导航栏子标签)
    """

    # 导航栏子标签名称
    name = models.CharField(max_length=16)

    # 父级导航栏
    navigation = models.ForeignKey(Navigation, on_delete=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"分类"
        verbose_name_plural = u"分类"


class Tag(models.Model):
    """
    标签
    """

    # 标签名称
    name = models.CharField(max_length=16)

    # 标签说明
    desc = models.CharField(max_length=64, blank=True)

    class Meta:
        verbose_name = u"标签"
        verbose_name_plural = u"标签"

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    文章
    """
    # 标题
    title = models.CharField(max_length=16, verbose_name="标题")

    # 文章内容(格式为markdown)
    body = MDTextField()

    # 文章摘要
    excerpt = models.CharField(max_length=128, blank=True, verbose_name="摘要")

    # 创建时间
    created_time = models.DateTimeField(blank=True, verbose_name="创建时间")

    # 修改时间
    modified_time = models.DateTimeField(blank=True, verbose_name="修改时间")

    # 文章所属分类(多对一)
    category = models.ForeignKey(Category, verbose_name="分类", on_delete=True)

    # 文章标签(多对的)
    tags = models.ManyToManyField(Tag, verbose_name="标签")

    # 作者(多对一)
    author = models.ForeignKey(User, verbose_name="作者", on_delete=True)

    # 阅读量
    view = models.PositiveIntegerField(default=0, verbose_name="阅读量")

    img = models.ImageField(upload_to='images', blank=True, verbose_name="缩略图")

    class Meta:
        ordering = ['-modified_time']
        verbose_name = u"文章"
        verbose_name_plural = u"文章"

    def __str__(self):
        return self.title

    def increase_view(self):
        self.view += 1
        self.save(update_fields=['view'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            self.excerpt = strip_tags(self.body)[:54]
            print(len(self.excerpt))

        if not self.created_time:
            self.created_time = datetime.datetime.now()
        self.modified_time = datetime.datetime.now()

        if not self.img:
            self.img = 'images/logo.jpg'

        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})


class DailySentence(models.Model):
    created_time = models.DateField(auto_now_add=True, verbose_name="创建时间")
    content = models.TextField(verbose_name='内容')

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-pk']
        verbose_name = u"每日一句"
        verbose_name_plural = u"每日一句"


class Broadcast(models.Model):
    image = models.ImageField(upload_to='images', verbose_name="图片")
    content = models.TextField(verbose_name='内容')
    post = models.ForeignKey(Post, verbose_name='文章详情', on_delete=True)
    modified_time = models.DateTimeField(blank=True, null=True, verbose_name='修改时间')
    is_activate = models.BooleanField(default=False, verbose_name='第一张')

    def save(self, *args, **kwargs):
        self.modified_time = datetime.datetime.now()
        super(Broadcast, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-modified_time']
        verbose_name = u'轮播图'
        verbose_name_plural = u'轮播图'
