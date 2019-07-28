from django.contrib import admin

# Register your models here.
from apps.staff.models import RoleTier, Role, Staff

@admin.register(RoleTier)
class RoleTierAdmin(admin.ModelAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass


