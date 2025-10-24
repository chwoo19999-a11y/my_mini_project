from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiParameter
from .models import Region, Destination
from .serializers import (
    RegionSerializer,
    DestinationListSerializer,
    DestinationDetailSerializer,
    DestinationCreateUpdateSerializer
)


class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    """지역 ViewSet (읽기 전용)"""
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @extend_schema(
        summary="지역 목록 조회",
        description="모든 지역(북인도/남인도) 목록을 조회합니다.",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="지역 상세 조회",
        description="특정 지역의 상세 정보를 조회합니다.",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class DestinationViewSet(viewsets.ModelViewSet):
    """여행지 ViewSet"""
    queryset = Destination.objects.select_related('region').prefetch_related('likes', 'comments')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['region']
    search_fields = ['name', 'name_en', 'description', 'address']
    ordering_fields = ['created_at', 'likes_count', 'view_count', 'comments_count']
    ordering = ['-created_at']

    def get_serializer_class(self):
        """액션별 Serializer 선택"""
        if self.action == 'list':
            return DestinationListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return DestinationCreateUpdateSerializer
        return DestinationDetailSerializer

    @extend_schema(
        summary="여행지 목록 조회",
        description="모든 여행지 목록을 조회합니다. 지역별 필터링, 검색, 정렬 가능합니다.",
        parameters=[
            OpenApiParameter(name='region', description='지역 ID로 필터링', required=False, type=int),
            OpenApiParameter(name='search', description='여행지명, 설명 등으로 검색', required=False, type=str),
            OpenApiParameter(name='ordering', description='정렬 기준 (-created_at, -likes_count, -view_count)', required=False, type=str),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="여행지 상세 조회",
        description="특정 여행지의 상세 정보를 조회합니다. 조회수가 1 증가합니다.",
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # 조회수 증가
        instance.increment_view_count()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @extend_schema(
        summary="여행지 생성",
        description="새로운 여행지를 생성합니다. (관리자 전용 - 현재는 인증된 사용자 모두 가능)",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="여행지 수정",
        description="여행지 정보를 수정합니다. (관리자 전용 - 현재는 인증된 사용자 모두 가능)",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="여행지 부분 수정",
        description="여행지 정보를 부분 수정합니다. (관리자 전용 - 현재는 인증된 사용자 모두 가능)",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="여행지 삭제",
        description="여행지를 삭제합니다. (관리자 전용 - 현재는 인증된 사용자 모두 가능)",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @extend_schema(
        summary="인기 여행지 조회",
        description="좋아요가 많은 인기 여행지 Top 10을 조회합니다.",
    )
    @action(detail=False, methods=['get'])
    def popular(self, request):
        """인기 여행지 (좋아요 순)"""
        destinations = self.get_queryset().order_by('-likes_count', '-view_count')[:10]
        serializer = DestinationListSerializer(destinations, many=True, context={'request': request})
        return Response(serializer.data)

    @extend_schema(
        summary="추천 여행지 조회",
        description="조회수가 많은 추천 여행지 Top 10을 조회합니다.",
    )
    @action(detail=False, methods=['get'])
    def recommended(self, request):
        """추천 여행지 (조회수 순)"""
        destinations = self.get_queryset().order_by('-view_count', '-likes_count')[:10]
        serializer = DestinationListSerializer(destinations, many=True, context={'request': request})
        return Response(serializer.data)
