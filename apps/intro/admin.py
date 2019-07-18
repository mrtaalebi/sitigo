from django.contrib import admin

from apps.intro.models import HomePageImage, HomePage


@admin.register(HomePageImage)
class HomePageImageAdmin(admin.ModelAdmin):
    fields = ['image', 'persian_caption', 'english_caption', 'homePage']


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    fields = ['sponsor_name_persian', 'sponsor_name_english', 'organizer_name_persian', 'organizer_name_english', 'sponsor_image', 'organizer_image' ]