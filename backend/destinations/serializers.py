from rest_framework import serializers
from .models import Region, Destination


class RegionSerializer(serializers.ModelSerializer):
    """지역 Serializer"""
    display_name = serializers.CharField(source='get_name_display', read_only=True)

    class Meta:
        model = Region
        fields = ['id', 'name', 'display_name', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']


class DestinationListSerializer(serializers.ModelSerializer):
    """여행지 목록 Serializer"""
    region_name = serializers.CharField(source='region.get_name_display', read_only=True)
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Destination
        fields = [
            'id', 'name', 'name_en', 'region', 'region_name',
            'image', 'description', 'likes_count', 'comments_count',
            'view_count', 'is_liked', 'created_at'
        ]
        read_only_fields = ['id', 'likes_count', 'comments_count', 'view_count', 'created_at']

    def get_is_liked(self, obj):
        """현재 사용자의 좋아요 여부"""
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(user=request.user).exists()
        return False


class DestinationDetailSerializer(serializers.ModelSerializer):
    """여행지 상세 Serializer"""
    region_name = serializers.CharField(source='region.get_name_display', read_only=True)
    region_info = RegionSerializer(source='region', read_only=True)
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Destination
        fields = [
            'id', 'name', 'name_en', 'region', 'region_name', 'region_info',
            'description', 'image', 'address', 'latitude', 'longitude',
            'likes_count', 'comments_count', 'view_count', 'is_liked',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'likes_count', 'comments_count', 'view_count', 'created_at', 'updated_at']

    def get_is_liked(self, obj):
        """현재 사용자의 좋아요 여부"""
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(user=request.user).exists()
        return False


class DestinationCreateUpdateSerializer(serializers.ModelSerializer):
    """여행지 생성/수정 Serializer"""

    class Meta:
        model = Destination
        fields = [
            'region', 'name', 'name_en', 'description', 'image',
            'address', 'latitude', 'longitude'
        ]

    def validate_name(self, value):
        """여행지명 검증"""
        if len(value.strip()) < 2:
            raise serializers.ValidationError('여행지명은 최소 2자 이상이어야 합니다.')
        return value

    def validate_description(self, value):
        """설명 검증"""
        if len(value.strip()) < 10:
            raise serializers.ValidationError('설명은 최소 10자 이상이어야 합니다.')
        return value
