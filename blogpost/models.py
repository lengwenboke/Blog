from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from mdeditor.fields import MDTextField


class Navigation(models.Model):
    """
    导航栏
    """
    # 导航栏名称
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    分类(导航栏子标签)
    """

    # 导航栏子标签名称
    name = models.CharField(max_length=16)

    # 父级导航栏
    navigation = models.ForeignKey(Navigation)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    标签
    """

    # 标签名称
    name = models.CharField(max_length=16)

    # 标签说明
    desc = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    文章
    """
    # 标题
    title = models.CharField(max_length=64)

    # 文章内容(格式为markdown)
    body = MDTextField()

    # 文章摘要
    excerpt = models.CharField(max_length=32)

    # 创建时间
    created_time = models.DateTimeField()

    # 修改时间
    modified_time = models.DateTimeField()

    # 文章所属分类(多对一)
    category = models.ForeignKey(Category)

    # 文章标签(多对的)
    tags = models.ManyToManyField(Tag)

    # 作者(多对一)
    author = models.ForeignKey(User)

    # 阅读量
    view = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
