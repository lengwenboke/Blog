from django.contrib import admin

# Register your models here.
from comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'email', 'author_reply', 'created_time', 'post')
    list_filter = ('name', 'email', 'created_time', 'post')
    readonly_fields = ('name', 'email', 'post', 'created_time', 'text')
    fields = ('name', 'email', 'post', 'created_time', ('text', 'author_reply'))


admin.site.register(Comment, CommentAdmin)
