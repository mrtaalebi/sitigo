from django.conf.urls import url
from django.urls import path, include
from apps.content import views

app_name = "content"
urlpatterns = [
    url(r'^download/$', views.doc_dwnldr),
    # url(r'^articles/(?P<category_id>\w+)/$', views.articles, name='articles'),
    # url(r'^articles/$', views.articles),
    # url(r'^(?P<event_id>\w+)/$', views.event),
    # url(r'^$', views.event),
]
