from rest_framework import serializers
from .models import Certificate

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'  # Все поля модели будут доступны через API
