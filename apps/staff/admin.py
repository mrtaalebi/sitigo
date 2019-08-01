from django.contrib import admin

# Register your models here.
from apps.staff.models import Team, Role, Staff

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass


