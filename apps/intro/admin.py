from django.contrib import admin

from .models import HomePageData, Organizer, Slide


@admin.register(HomePageData)
class HomePageDataAdmin(admin.ModelAdmin):
    pass


@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    pass


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    pass
