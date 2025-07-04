from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = BaseUserAdmin.list_display + ('date_of_birth', 'is_doctor', 'hospital', 'position', 'phone_number')
    ordering = ('-date_joined',)

admin.site.register(User, UserAdmin)