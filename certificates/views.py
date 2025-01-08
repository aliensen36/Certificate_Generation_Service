from rest_framework import viewsets
from .models import Certificate
from .serializers import CertificateSerializer

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()  # Все объекты сертификатов
    serializer_class = CertificateSerializer
