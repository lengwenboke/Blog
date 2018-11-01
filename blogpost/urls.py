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
    url(r'^category/(?P<pk>[0-9]+)/$', CategoryView.as_view(), name='category'),
    url(r'^navigation/(?P<pk>[0-9]+)/$', NavigationView.as_view(), name='navigation'),
    url(r'^tags/$', TagsView.as_view(), name='tags'),
    url(r'^tagsfilter/(?P<pk>[0-9]+)/$', TagsFilterView.as_view(), name='tagsfilter'),
]
