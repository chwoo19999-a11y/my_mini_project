from django.contrib import admin
from django.utils.html import format_html
from .models import Region, Destination


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['get_name_display', 'description', 'created_at']
    search_fields = ['name', 'description']
    ordering = ['name']


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'region', 'get_image_preview', 'likes_count', 'comments_count', 'view_count', 'created_at']
    list_filter = ['region', 'created_at']
    search_fields = ['name', 'name_en', 'description', 'address']
    readonly_fields = ['likes_count', 'comments_count', 'view_count', 'created_at', 'updated_at', 'get_image_preview']
    ordering = ['-created_at']

    fieldsets = (
        ('기본 정보', {
            'fields': ('region', 'name', 'name_en', 'description')
        }),
        ('이미지', {
            'fields': ('image', 'get_image_preview')
        }),
        ('위치 정보', {
            'fields': ('address', 'latitude', 'longitude')
        }),
        ('통계', {
            'fields': ('likes_count', 'comments_count', 'view_count')
        }),
        ('일자', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def get_image_preview(self, obj):
        """이미지 미리보기"""
        if obj.image:
            return format_html(
                '<img src="{}" width="200" style="border-radius: 8px;" />',
                obj.image.url
            )
        return '-'
    get_image_preview.short_description = '이미지 미리보기'
