from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_spectacular.utils import extend_schema, OpenApiResponse
from .models import User
from .serializers import (
    UserSerializer,
    UserRegistrationSerializer,
    UserProfileSerializer,
    ChangePasswordSerializer,
    CustomTokenObtainPairSerializer
)


class RegisterView(generics.CreateAPIView):
    """회원가입 API"""
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer

    @extend_schema(
        summary="회원가입",
        description="새로운 사용자를 등록합니다.",
        responses={
            201: OpenApiResponse(response=UserSerializer, description="회원가입 성공"),
            400: OpenApiResponse(description="입력 데이터 오류"),
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            UserSerializer(user).data,
            status=status.HTTP_201_CREATED
        )


class CustomTokenObtainPairView(TokenObtainPairView):
    """로그인 API (JWT 토큰 발급)"""
    serializer_class = CustomTokenObtainPairSerializer

    @extend_schema(
        summary="로그인",
        description="사용자 인증 후 JWT 토큰을 발급합니다.",
        responses={
            200: OpenApiResponse(description="로그인 성공"),
            401: OpenApiResponse(description="인증 실패"),
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ProfileView(generics.RetrieveUpdateAPIView):
    """프로필 조회/수정 API"""
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user

    @extend_schema(
        summary="프로필 조회",
        description="현재 로그인한 사용자의 프로필 정보를 조회합니다.",
        responses={
            200: OpenApiResponse(response=UserProfileSerializer, description="조회 성공"),
            401: OpenApiResponse(description="인증 필요"),
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="프로필 수정",
        description="현재 로그인한 사용자의 프로필 정보를 수정합니다.",
        responses={
            200: OpenApiResponse(response=UserProfileSerializer, description="수정 성공"),
            400: OpenApiResponse(description="입력 데이터 오류"),
            401: OpenApiResponse(description="인증 필요"),
        }
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


@extend_schema(
    summary="비밀번호 변경",
    description="현재 로그인한 사용자의 비밀번호를 변경합니다.",
    request=ChangePasswordSerializer,
    responses={
        200: OpenApiResponse(description="비밀번호 변경 성공"),
        400: OpenApiResponse(description="입력 데이터 오류"),
        401: OpenApiResponse(description="인증 필요"),
    }
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    """비밀번호 변경 API"""
    serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response({'message': '비밀번호가 성공적으로 변경되었습니다.'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
