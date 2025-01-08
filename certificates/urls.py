from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CertificateViewSet

# Используем роутер для автоматической генерации маршрутов
router = DefaultRouter()
router.register(r'certificates', CertificateViewSet, basename='certificate')

urlpatterns = [
    path('', include(router.urls)),  # Включаем все маршруты, сгенерированные роутером
]
