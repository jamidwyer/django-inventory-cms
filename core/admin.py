from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'first_name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'first_name',
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',

            ),
        }),
    )


admin.site.register(User, UserAdmin)
