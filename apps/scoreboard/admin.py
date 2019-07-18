from django.contrib import admin

from .models import Contestant, Country, Ruler, ProblemScore, ContestTier, CSV


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

@admin.register(CSV)
class CSVAdmin(admin.ModelAdmin):
    fields = ['csv_file', 'contest_tier']

