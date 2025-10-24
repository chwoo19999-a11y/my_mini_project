from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegionViewSet, DestinationViewSet

router = DefaultRouter()
router.register('regions', RegionViewSet, basename='region')
router.register('destinations', DestinationViewSet, basename='destination')

urlpatterns = [
    path('', include(router.urls)),
]
