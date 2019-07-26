from django.contrib import admin

from .models import Image, CountryEvent, Country


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
        pass

@admin.register(CountryEvent)
class CountryEventAdmin(admin.ModelAdmin):
        pass

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
        pass

