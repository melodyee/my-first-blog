"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin

from . import view, testdb
from blog import views

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]
# from HelloWorld import search, search2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello$', view.hello, name='home'),
    url(r'^testdb$', testdb.testdb),
    # url(r'^search_form$', search.search_form),
    # url(r'^search$', search.search),
    # url(r'^search_post$', search2.search_post),
    url(r'^post$', views.post_list, name='post_list'),
    # url(r'^post$', include('blog.urls')),
    url(r'^post_bymonth/(?P<pk>.+)/$', views.post_month, name='post_month'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^polls/', include('polls.urls')),

    url(r'^bootstrap-basic$', view.bootstrap, name='bootstrap-basic'),
    url(r'^bootstrap-form$', view.bootstrapform, name='bootstrap-form'),
    url(r'^bootstrap-demo$', view.bootstrapdemo, name='bootstrap-demo'),

]
