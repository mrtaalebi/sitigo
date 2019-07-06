from django.conf.urls import url
from django.urls import path, include
from apps.staff import views


app_name = "staff"
urlpatterns = [
    url(r'^(?P<event_id>\w+)/$', views.staff),
    url(r'^$', views.staff),
]
