from django.contrib import admin

from .models import *


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    # listdisplay设置要显示在列表中的字段
    list_display = ('title', 'modified_time', 'author')

    ordering = ('-modified_time',)

    fields = ('title', 'body', 'img', 'category', 'tags', 'author')

    search_fields = ['title', 'body', ]

    list_filter = ('title', 'category', 'tags', 'author')
    filter_horizontal = ('tags',)


class DailySentenceAdmin(admin.ModelAdmin):
    list_display = ('created_time', 'content')
    search_fields = ['content']
    fields = ('content',)
    list_filter = ('created_time',)


class BroadcastAdmin(admin.ModelAdmin):
    list_display = ('post', 'content', 'image', 'modified_time', 'is_activate')
    fields = ('image', 'content', 'post', 'is_activate')


# image = models.ImageField(upload_to='images', verbose_name="图片")
# content = models.TextField(verbose_name='内容')
# post = models.ForeignKey(Post, verbose_name='文章详情')

admin.site.site_header = "冷文博客后台管理"
admin.site.site_title = "冷文博客"

admin.site.register(Post, PostAdmin)
admin.site.register(Navigation)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(DailySentence, DailySentenceAdmin)
admin.site.register(Broadcast, BroadcastAdmin)
