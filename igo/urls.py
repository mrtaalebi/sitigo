
"""igo URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, i18n
from django.contrib import admin
from django.urls import path, include
from apps.intro import urls as intro_urls
from apps.intro.views import set_lang
from apps.content import urls as content_urls, views
from apps.contact_us import urls as contact_us_urls
from apps.blog import urls as blog_urls
from apps.question import urls as question_urls
from apps.staff import urls as staff_url
from apps.scoreboard import urls as scoreboard_urls
from apps.gallery import urls as gallery_urls

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^set_lang/', set_lang),
    url(r'^faq/', include(question_urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^content/', include(content_urls)),
    url(r'^', include(intro_urls), name='intro'),
    url(r'^contact_us/', include(contact_us_urls)),
    url(r'^blog/', include(blog_urls), name='blog'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^staff/', include(staff_url)),
    url(r'^events/(?P<event_id>\d+)/$', views.event),
    url(r'^events/$', views.event),
    url(r'^articles/(?P<category_id>\d+)/$', views.articles),
    url(r'^articles/$', views.articles),

    url(r'^scoreboard/', include(scoreboard_urls), name='scoreboard'),
    url(r'^gallery/', include(gallery_urls), name='gallery'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

