from django.contrib import admin
from .models import Like, Comment


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'destination', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'destination__name']
    readonly_fields = ['created_at']
    ordering = ['-created_at']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'destination', 'get_content_preview', 'parent', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'destination__name', 'content']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']

    fieldsets = (
        ('댓글 정보', {
            'fields': ('destination', 'user', 'content', 'parent')
        }),
        ('일자', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def get_content_preview(self, obj):
        """댓글 내용 미리보기"""
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    get_content_preview.short_description = '내용'
