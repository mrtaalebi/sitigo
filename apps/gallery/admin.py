from django.contrib import admin

from .models import Image, CountryEvent, Country, City, Gallery, GroupImageUpload


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    search_fields = ['image__name']
    pass


@admin.register(CountryEvent)
class CountryEventAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(GroupImageUpload)
class GroupImageUploadAdmin(admin.ModelAdmin):
    pass

