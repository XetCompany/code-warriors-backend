from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import Request, Notification, User

admin.site.register(Request)
admin.site.register(Notification)

class CustomUserAdmin(UserAdmin):
    """ Кастомное отоброжение модели юзера в бд"""
    model = User
    list_display = ('username', 'id', 'is_staff', 'is_active',)
    list_filter = ('username', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': (
            'username',
            'email',
            'fullname',
            'phone',
            'description',
            'password')
        }),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'fullname',
                'phone',
                'description',
                'is_staff',
                'is_active'
            )
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(User, CustomUserAdmin)