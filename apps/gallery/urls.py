from django.conf.urls import url
from django.urls import path, include
from apps.gallery import views


app_name = "gallery"

urlpatterns = [
    url(r'^(?P<event_id>\d+)/$', views.gallery, name='gallery'),
    url(r'^/$', views.gallery, name='gallery'),
]

