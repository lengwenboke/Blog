from django.conf.urls import url
from django.conf.urls.static import static
from django.views.static import serve

from Blog import settings
from Blog.settings import MEDIA_ROOT
from .views import *

app_name = 'blog'
urlpatterns = [
                  url(r'^$', IndexView.as_view(), name="index"),
                  url(r'^post/(?P<pk>[0-9]+)/$', PostDetailView.as_view(), name="detail"),
                  # url(r'^uploads/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
              ]
