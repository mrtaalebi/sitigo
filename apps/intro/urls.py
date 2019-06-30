from django.urls import path
from apps.intro import views

urlpatterns = [
    path('', views.homepage)
]