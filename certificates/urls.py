from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Роутер для автоматической генерации маршрутов
router = DefaultRouter()
router.register('owners', OwnerViewSet)
router.register('roles', RoleViewSet)
router.register('skill-categories', SkillCategoryViewSet)
router.register('skills', SkillViewSet)
router.register(r'certificates', CertificateViewSet, basename='certificate')

urlpatterns = [
    path('', include(router.urls)),
]
