from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError


class Like(models.Model):
    """좋아요"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name='사용자'
    )
    destination = models.ForeignKey(
        'destinations.Destination',
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name='여행지'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')

    class Meta:
        db_table = 'likes'
        verbose_name = '좋아요'
        verbose_name_plural = '좋아요 목록'
        unique_together = [['user', 'destination']]
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', '-created_at']),
            models.Index(fields=['destination']),
        ]

    def __str__(self):
        return f"{self.user.username} likes {self.destination.name}"


class Comment(models.Model):
    """댓글"""
    destination = models.ForeignKey(
        'destinations.Destination',
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='여행지'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='작성자'
    )
    content = models.TextField(
        validators=[MinLengthValidator(1, '댓글 내용을 입력해주세요.')],
        verbose_name='내용'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies',
        verbose_name='부모 댓글'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')

    class Meta:
        db_table = 'comments'
        verbose_name = '댓글'
        verbose_name_plural = '댓글 목록'
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['destination', 'created_at']),
            models.Index(fields=['user', '-created_at']),
        ]

    def __str__(self):
        return f"{self.user.username}: {self.content[:50]}"

    def clean(self):
        """모델 레벨 검증"""
        super().clean()

        # 대댓글의 대댓글 방지 (1단계만 허용)
        if self.parent and self.parent.parent:
            raise ValidationError({'parent': '대댓글의 대댓글은 작성할 수 없습니다.'})

        # 부모 댓글과 같은 여행지인지 확인
        if self.parent and self.parent.destination != self.destination:
            raise ValidationError({'parent': '부모 댓글과 같은 여행지여야 합니다.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
