from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import CategoryRequest, Photo, Video, Request, Notification, User, ResetPasswordToken, Response, Review, \
    Message

admin.site.register(CategoryRequest)
admin.site.register(Review)
admin.site.register(Response)
admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(Request)
admin.site.register(Notification)
admin.site.register(ResetPasswordToken)
admin.site.register(Message)


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
            'chosen_categories',
            'photos',
            'videos',
            'notifications',
            'password',
            'groups',
            'is_buy_update',
            'buy_update_to'
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
                'chosen_categories',
                'photos',
                'videos',
                'notifications',
                'password1',
                'password2',
                'is_staff',
                'is_active',
                'is_buy_update',
                'buy_update_to'
            )
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(User, CustomUserAdmin)
