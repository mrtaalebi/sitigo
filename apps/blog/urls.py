from django.conf.urls import url
from django.urls import path, include
from apps.blog import views


app_name = 'blog'

urlpatterns = [
    url(r'^(?P<dir_id>\d+)/(?P<post_id>\d+)/$', views.blog_post, name="blog_post"),
    url(r'^(?P<dir_id>\d+)/$', views.blog_dir, name="blog_dir"),
    url(r'^$', views.blog_dir, name="blog_dir"),
    url(r'^subscribe$', views.subscribe, name='subscribe'),
    url(r'^leave_comment/(?P<dir_id>\d+)/(?P<post_id>\d+)/$', views.leave_comment, name='leave_comment'),

]
