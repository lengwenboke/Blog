from django.contrib import admin

# Register your models here.
from comments.models import *


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'email', 'author_reply', 'created_time', 'post')
    list_filter = ('name', 'email', 'created_time', 'post')
    readonly_fields = ('name', 'email', 'post', 'created_time', 'text')
    fields = ('name', 'email', 'post', 'created_time', ('text', 'author_reply'))
    search_fields = ['name', 'text', 'email']


class FriendlyAdmin(admin.ModelAdmin):
    list_display = ('title', 'weburl', 'email', 'created_time', 'modified_time', 'flag')
    list_filter = ('created_time', 'modified_time', 'flag')
    readonly_fields = ('title', 'weburl', 'email', 'created_time', 'modified_time', 'desc', 'reason')
    fields = ('title', 'weburl', 'email', 'created_time', 'modified_time', 'desc', 'reason', 'flag')
    search_fields = ['title', 'weburl', 'email']


class LmsgAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'text', 'created_time')
    list_filter = ('created_time', 'email')
    readonly_fields = ('name', 'email', 'text', 'created_time')
    search_fields = ['name', 'email', 'text']


# name = models.CharField(max_length=32, verbose_name="昵称")
# email = models.EmailField(max_length=64, verbose_name="邮箱")
# text = models.TextField(verbose_name="留言内容")
# created_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")


admin.site.register(Comment, CommentAdmin)
admin.site.register(Friendly, FriendlyAdmin)
admin.site.register(Lmsg, LmsgAdmin)
