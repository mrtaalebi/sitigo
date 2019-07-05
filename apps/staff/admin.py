from django.contrib import admin

# Register your models here.
from apps.staff.models import Role, Staff


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    fields = ['persian_name', 'english_name']


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    fields = ['event', 'persian_name', 'english_name', 'role', 'image']
