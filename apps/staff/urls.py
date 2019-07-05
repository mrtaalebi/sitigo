from django.conf.urls import url
from django.urls import path, include
from apps.staff import views


app_name = "staff"
urlpatterns = [
    url(r'^$', views.staff),
]
