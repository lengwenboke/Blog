"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve

from Blog.settings import MEDIA_ROOT
from blogpost.feed import AllPostsRssFeed

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'mdeditor/', include('mdeditor.urls')),
    url(r'', include('blogpost.urls')),
    url(r'', include('comments.urls')),
    # url(r'^search/', include('haystack.urls')),
    url(r'^all/rss$', AllPostsRssFeed(), name='rss'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
