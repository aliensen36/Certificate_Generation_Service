from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class OwnerViewSet(ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class SkillCategoryViewSet(ModelViewSet):
    queryset = SkillCategory.objects.prefetch_related('skills')  # Предзагрузка связанных данных
    serializer_class = SkillCategorySerializer


class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.select_related('category')  # Предзагрузка связанных категорий
    serializer_class = SkillSerializer


class CriterionViewSet(ModelViewSet):
    queryset = Criterion.objects.all()
    serializer_class = CriterionSerializer


class ScoreViewSet(ModelViewSet):
    queryset = Score.objects.select_related('owner', 'certificate', 'criterion')
    serializer_class = ScoreSerializer


class CertificateViewSet(ModelViewSet):
    queryset = Certificate.objects.select_related('owner', 'role') \
                                   .prefetch_related('skills', 'scores__criterion')
    serializer_class = CertificateSerializer
