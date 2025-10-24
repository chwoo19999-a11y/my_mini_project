from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'get_profile_image', 'is_staff', 'created_at']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'created_at']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at', 'last_login', 'date_joined']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('개인정보', {'fields': ('first_name', 'last_name', 'email', 'bio', 'profile_image')}),
        ('권한', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('중요한 일자', {'fields': ('last_login', 'date_joined', 'created_at', 'updated_at')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

    def get_profile_image(self, obj):
        """프로필 이미지 미리보기"""
        if obj.profile_image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 50%;" />',
                obj.profile_image.url
            )
        return '-'
    get_profile_image.short_description = '프로필 이미지'
