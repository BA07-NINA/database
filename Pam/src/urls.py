from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.deployment import DeploymentViewSet
from api.media import MediaViewSet
from api.user import UserViewSet

router = DefaultRouter()
router.register(r'deployments', DeploymentViewSet, basename='deployment')
router.register(r'media', MediaViewSet, basename='media')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('api/', include(router.urls)),
]
