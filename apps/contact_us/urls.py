from django.conf.urls import url
from django.urls import path, include
from apps.contact_us import views


app_name = "contact_us"

urlpatterns = [
    url(r'', views.contact_us, name='contact_us'),

]

