from rest_framework import serializers
from .models import Like, Comment
from accounts.serializers import UserSerializer


class LikeSerializer(serializers.ModelSerializer):
    """좋아요 Serializer"""
    user_info = UserSerializer(source='user', read_only=True)
    destination_name = serializers.CharField(source='destination.name', read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'user', 'user_info', 'destination', 'destination_name', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    """댓글 Serializer"""
    user_info = UserSerializer(source='user', read_only=True)
    replies = serializers.SerializerMethodField()
    replies_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id', 'destination', 'user', 'user_info', 'content',
            'parent', 'replies', 'replies_count', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def get_replies(self, obj):
        """대댓글 목록"""
        if obj.parent is None:  # 최상위 댓글만 대댓글을 가져옴
            replies = obj.replies.all()
            return CommentSerializer(replies, many=True, context=self.context).data
        return []

    def get_replies_count(self, obj):
        """대댓글 개수"""
        if obj.parent is None:
            return obj.replies.count()
        return 0

    def validate_content(self, value):
        """댓글 내용 검증"""
        if len(value.strip()) < 1:
            raise serializers.ValidationError('댓글 내용을 입력해주세요.')
        if len(value) > 1000:
            raise serializers.ValidationError('댓글은 1000자를 초과할 수 없습니다.')
        return value

    def validate(self, attrs):
        """댓글 검증"""
        # 대댓글의 대댓글 방지
        parent = attrs.get('parent')
        if parent and parent.parent:
            raise serializers.ValidationError({'parent': '대댓글의 대댓글은 작성할 수 없습니다.'})

        # 부모 댓글과 같은 여행지인지 확인
        destination = attrs.get('destination')
        if parent and parent.destination != destination:
            raise serializers.ValidationError({'parent': '부모 댓글과 같은 여행지여야 합니다.'})

        return attrs


class CommentCreateSerializer(serializers.ModelSerializer):
    """댓글 생성 Serializer"""

    class Meta:
        model = Comment
        fields = ['destination', 'content', 'parent']

    def validate_content(self, value):
        """댓글 내용 검증"""
        if len(value.strip()) < 1:
            raise serializers.ValidationError('댓글 내용을 입력해주세요.')
        if len(value) > 1000:
            raise serializers.ValidationError('댓글은 1000자를 초과할 수 없습니다.')
        return value

    def validate(self, attrs):
        """댓글 검증"""
        parent = attrs.get('parent')
        if parent and parent.parent:
            raise serializers.ValidationError({'parent': '대댓글의 대댓글은 작성할 수 없습니다.'})

        destination = attrs.get('destination')
        if parent and parent.destination != destination:
            raise serializers.ValidationError({'parent': '부모 댓글과 같은 여행지여야 합니다.'})

        return attrs
