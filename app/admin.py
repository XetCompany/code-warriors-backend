from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import CategoryRequest, Photo, Video, Request, Notification, User, ResetPasswordToken

admin.site.register(CategoryRequest)
admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(Request)
admin.site.register(Notification)
admin.site.register(ResetPasswordToken)


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
            'notifications',
            'password',
            'groups',
        )
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
                'password1',
                'password2',
                'notifications',
                'is_staff',
                'is_active'
            )
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(User, CustomUserAdmin)
