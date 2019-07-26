from django.conf.urls import url
from django.urls import path, include
from apps.scoreboard import views


app_name = "scoreboard"

urlpatterns = [
    url(r'^(?P<event_id>\d+)/$', views.scoreboard, name='scoreboard'),
    url(r'^/$', views.scoreboard, name='scoreboard'),
]

