from django.contrib import admin
from .models import *


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department',)


admin.site.register(Department, DepartmentAdmin)


class DivisionAdmin(admin.ModelAdmin):
    list_display = ('division',)


admin.site.register(Division, DivisionAdmin)


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('phone',)


admin.site.register(Phone, PhoneAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'is_published')
    # search_fields = ('name', 'department')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'department')


admin.site.register(Employee, EmployeeAdmin)
