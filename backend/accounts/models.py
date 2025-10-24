from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


def validate_image_size(file):
    """이미지 파일 크기 검증 (5MB 제한)"""
    from django.conf import settings
    max_size = getattr(settings, 'MAX_IMAGE_SIZE', 5 * 1024 * 1024)
    if file.size > max_size:
        raise ValidationError(f'파일 크기는 {max_size / (1024 * 1024)}MB를 초과할 수 없습니다.')


class User(AbstractUser):
    """사용자 모델"""
    email = models.EmailField(unique=True, verbose_name='이메일')
    profile_image = models.ImageField(
        upload_to='profiles/%Y/%m/%d/',
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp']),
            validate_image_size
        ],
        verbose_name='프로필 이미지'
    )
    bio = models.TextField(max_length=500, blank=True, verbose_name='자기소개')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='가입일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')

    class Meta:
        db_table = 'users'
        verbose_name = '사용자'
        verbose_name_plural = '사용자 목록'
        ordering = ['-created_at']

    def __str__(self):
        return self.username
