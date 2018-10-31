from django.conf.urls import url
from .views import *

app_name = 'blog'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^post/(?P<pk>[0-9]+)/$', PostDetailView.as_view(), name="detail")
]
