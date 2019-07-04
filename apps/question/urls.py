from django.conf.urls import url
from django.urls import path, include
from apps.question import views


app_name = "question"
urlpatterns = [
    url(r'^$', views.question_answer),
]
