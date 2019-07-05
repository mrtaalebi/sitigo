from django.conf.urls import url
from django.urls import path, include
from apps.contact_us import views


app_name = "contact_us"

urlpatterns = [
<<<<<<< HEAD
    url('contact_us/', views.contact_us, name='contact_us'),
    url('sent/', views.sent, name='sent')
=======
    url(r'', views.contact_us, name='contact_us'),

>>>>>>> 2d278b134f59c8755fcbaa0e67b816006646c813
]

