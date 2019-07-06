from django.conf.urls import url
from django.urls import path, include
from apps.blog import views


app_name = 'blog'

urlpatterns = [
    url(r'^(?P<dir_id>\w+)/(?P<post_id>\w+)/$', views.blog_post, name="blog_post"),
    url(r'^(?P<dir_id>\w+)/$', views.blog_dir, name="blog_dir"),
    url(r'^$', views.blog_dir, name="blog_dir"),
    url(r'^subscription$', views.subscripted, name='subscripted'),
    url(r'^subscribe$', views.subscribe, name='subscribe')
   
]
