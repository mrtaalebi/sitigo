from django.contrib import admin

from .models import Contestant, Country, Ruler, ProblemScore, ContestTier


@admin.register(Contestant)
class ContestantAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Ruler)
class RulerAdmin(admin.ModelAdmin):
    pass


@admin.register(ProblemScore)
class ProblemScoreAdmin(admin.ModelAdmin):
    pass


@admin.register(ContestTier)
class ContestTierAdmin(admin.ModelAdmin):
    pass

