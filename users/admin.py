from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'is_doctor',
        'hospital',
        'phone_number',
        'date_of_birth',
        'created_at',
    )

    search_fields = ('username', 'email', 'hospital')

    list_filter = (
        'is_doctor',
    )
    ordering = ('-created_at',)