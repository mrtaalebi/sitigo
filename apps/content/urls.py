from django.conf.urls import url
from django.urls import path, include
from apps.content import views


app_name = "content"
urlpatterns = [
    url(r'$', views.age),
]
