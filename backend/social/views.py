from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from drf_spectacular.utils import extend_schema, OpenApiResponse
from .models import Like, Comment
from .serializers import LikeSerializer, CommentSerializer, CommentCreateSerializer
from destinations.models import Destination


class LikeViewSet(viewsets.ModelViewSet):
    """좋아요 ViewSet"""
    queryset = Like.objects.select_related('user', 'destination')
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """현재 사용자의 좋아요만 조회"""
        return self.queryset.filter(user=self.request.user)

    @extend_schema(
        summary="내 좋아요 목록 조회",
        description="현재 로그인한 사용자가 좋아요한 여행지 목록을 조회합니다.",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="좋아요 추가",
        description="여행지에 좋아요를 추가합니다.",
    )
    def create(self, request, *args, **kwargs):
        destination_id = request.data.get('destination')

        # 중복 확인
        if Like.objects.filter(user=request.user, destination_id=destination_id).exists():
            return Response(
                {'detail': '이미 좋아요한 여행지입니다.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        summary="좋아요 삭제",
        description="여행지의 좋아요를 취소합니다.",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @extend_schema(
        summary="여행지 좋아요 토글",
        description="여행지의 좋아요를 토글합니다. (있으면 삭제, 없으면 생성)",
    )
    @action(detail=False, methods=['post'])
    def toggle(self, request):
        """좋아요 토글 (추가/삭제)"""
        destination_id = request.data.get('destination')

        if not destination_id:
            return Response(
                {'detail': 'destination 필드가 필요합니다.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            destination = Destination.objects.get(id=destination_id)
        except Destination.DoesNotExist:
            return Response(
                {'detail': '존재하지 않는 여행지입니다.'},
                status=status.HTTP_404_NOT_FOUND
            )

        like, created = Like.objects.get_or_create(
            user=request.user,
            destination=destination
        )

        if not created:
            # 이미 존재하면 삭제
            like.delete()
            return Response(
                {'message': '좋아요가 취소되었습니다.', 'is_liked': False},
                status=status.HTTP_200_OK
            )

        # 새로 생성
        return Response(
            {'message': '좋아요가 추가되었습니다.', 'is_liked': True},
            status=status.HTTP_201_CREATED
        )


class CommentViewSet(viewsets.ModelViewSet):
    """댓글 ViewSet"""
    queryset = Comment.objects.select_related('user', 'destination', 'parent').prefetch_related('replies')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """부모 댓글만 조회 (대댓글은 serializer에서 처리)"""
        queryset = self.queryset.filter(parent__isnull=True)

        # destination 파라미터로 필터링
        destination_id = self.request.query_params.get('destination')
        if destination_id:
            queryset = queryset.filter(destination_id=destination_id)

        return queryset.order_by('created_at')

    def get_serializer_class(self):
        """액션별 Serializer 선택"""
        if self.action == 'create':
            return CommentCreateSerializer
        return CommentSerializer

    @extend_schema(
        summary="댓글 목록 조회",
        description="여행지의 댓글 목록을 조회합니다. destination 파라미터로 필터링 가능합니다.",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="댓글 상세 조회",
        description="특정 댓글의 상세 정보를 조회합니다.",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="댓글 작성",
        description="여행지에 댓글을 작성합니다. parent 필드로 대댓글 작성 가능합니다.",
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        # 응답은 CommentSerializer로
        response_serializer = CommentSerializer(serializer.instance, context={'request': request})
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        summary="댓글 수정",
        description="자신이 작성한 댓글을 수정합니다.",
    )
    def update(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.user != request.user:
            return Response(
                {'detail': '본인이 작성한 댓글만 수정할 수 있습니다.'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="댓글 부분 수정",
        description="자신이 작성한 댓글을 부분 수정합니다.",
    )
    def partial_update(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.user != request.user:
            return Response(
                {'detail': '본인이 작성한 댓글만 수정할 수 있습니다.'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="댓글 삭제",
        description="자신이 작성한 댓글을 삭제합니다.",
    )
    def destroy(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.user != request.user:
            return Response(
                {'detail': '본인이 작성한 댓글만 삭제할 수 있습니다.'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().destroy(request, *args, **kwargs)
