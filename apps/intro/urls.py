from django.conf.urls import url
from django.urls import path, include
from apps.intro import views
from django.conf.urls import i18n as i18n_url
app_name = "intro"
urlpatterns = [
    url(r'$', views.homepage),
    # url(r'^i18n/', include(i18n_url), name='i18n'),
]