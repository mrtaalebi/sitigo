from django.contrib import admin

from apps.intro.models import HomePageImage, HomePage


@admin.register(HomePageImage)
class HomePageImageAdmin(admin.ModelAdmin):
    fields = ['image', 'homePage']


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    pass