from django.contrib.auth.admin import UserAdmin, Group
from django.contrib.auth.models import Group
from django.contrib import admin

from accounts.models import User

class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active', 'is_school']
    list_filter = ['email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active', 'is_school']

    fieldsets = (
        (None, {"fields": ('email', 'first_name', 'last_name', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_school')}),
        ('Other Information', {'fields': ('date_joined', 'last_login')})
    )

    add_fieldsets = (
        (None, {"fields": ('email', 'first_name', 'last_name')}),
        ('Security', {'fields': ('password1', 'password2')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_school')}),
    )

admin.site.register(User, UserAdminConfig)
admin.site.unregister(Group)
