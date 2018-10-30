from django.contrib import admin

from .models import *

# Register your models here.

admin.site.site_header = "冷文博客后台管理"
admin.site.site_title = "冷文博客"



admin.site.register(Post)
admin.site.register(Navigation)
admin.site.register(Tag)
admin.site.register(Category)
