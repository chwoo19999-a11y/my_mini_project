from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator, MinLengthValidator
from django.core.exceptions import ValidationError


def validate_image_size(file):
    """이미지 파일 크기 검증 (5MB 제한)"""
    max_size = getattr(settings, 'MAX_IMAGE_SIZE', 5 * 1024 * 1024)
    if file.size > max_size:
        raise ValidationError(f'파일 크기는 {max_size / (1024 * 1024)}MB를 초과할 수 없습니다.')


class Region(models.Model):
    """지역 (북인도/남인도)"""
    NORTH = 'north'
    SOUTH = 'south'

    REGION_CHOICES = [
        (NORTH, '북인도'),
        (SOUTH, '남인도'),
    ]

    name = models.CharField(max_length=50, choices=REGION_CHOICES, unique=True, verbose_name='지역명')
    description = models.TextField(blank=True, verbose_name='지역 설명')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')

    class Meta:
        db_table = 'regions'
        verbose_name = '지역'
        verbose_name_plural = '지역 목록'
        ordering = ['name']

    def __str__(self):
        return self.get_name_display()


class Destination(models.Model):
    """여행지"""
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name='destinations',
        verbose_name='지역'
    )
    name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, '여행지명은 최소 2자 이상이어야 합니다.')],
        verbose_name='여행지명'
    )
    name_en = models.CharField(max_length=200, blank=True, verbose_name='영문명')
    description = models.TextField(
        validators=[MinLengthValidator(10, '설명은 최소 10자 이상이어야 합니다.')],
        verbose_name='설명'
    )
    image = models.ImageField(
        upload_to='destinations/%Y/%m/%d/',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp']),
            validate_image_size
        ],
        blank=True,
        null=True,
        verbose_name='대표 이미지'
    )
    address = models.CharField(max_length=500, blank=True, verbose_name='주소')
    latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True, verbose_name='위도')
    longitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True, verbose_name='경도')

    likes_count = models.PositiveIntegerField(default=0, verbose_name='좋아요 수')
    comments_count = models.PositiveIntegerField(default=0, verbose_name='댓글 수')
    view_count = models.PositiveIntegerField(default=0, verbose_name='조회수')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')

    class Meta:
        db_table = 'destinations'
        verbose_name = '여행지'
        verbose_name_plural = '여행지 목록'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['region', '-created_at']),
            models.Index(fields=['-likes_count']),
            models.Index(fields=['-view_count']),
        ]

    def __str__(self):
        return f"{self.name} ({self.region.get_name_display()})"

    def clean(self):
        """모델 레벨 검증"""
        super().clean()
        if self.name and len(self.name.strip()) < 2:
            raise ValidationError({'name': '여행지명은 공백을 제외하고 최소 2자 이상이어야 합니다.'})

    def save(self, *args, **kwargs):
        # full_clean()은 필요할 때만 명시적으로 호출
        # get_or_create 등에서 자동 검증으로 인한 문제 방지
        super().save(*args, **kwargs)

    def increment_view_count(self):
        """조회수 증가"""
        self.view_count += 1
        self.save(update_fields=['view_count'])
