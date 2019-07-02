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
from apps.intro import urls as intro_urls, views
from apps.intro.views import set_lang
from apps.content import urls as content_urls
from apps.contact_us import urls as contact_us_urls

from igo import settings
from django.conf.urls.static import static

urlpatterns = [
    path('set_lang/', views.set_lang),
    path('admin/', admin.site.urls),
    path('content/', include(content_urls)),
    path('intro/', include(intro_urls)),
    path('contact_us/', include(contact_us_urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

