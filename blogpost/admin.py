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


admin.site.site_header = "冷文博客后台管理"
admin.site.site_title = "冷文博客"

admin.site.register(Post, PostAdmin)
admin.site.register(Navigation)
admin.site.register(Tag)
admin.site.register(Category)
