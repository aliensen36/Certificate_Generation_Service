from rest_framework import serializers
from .models import *

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'




# Сериализатор для модели владельца
class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id', 'name', 'last_name', 'email']


# Сериализатор для модели роли
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']


# Сериализатор для модели навыка
class SkillSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)  # Человекочитаемая категория

    class Meta:
        model = Skill
        fields = ['id', 'name', 'category']


# Сериализатор для модели категории навыка
class SkillCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCategory
        fields = ['id', 'name']




# Сериализатор для модели Criterion
class CriterionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criterion
        fields = ['id', 'name']


# Сериализатор для модели Score
class ScoreSerializer(serializers.ModelSerializer):
    criterion = CriterionSerializer()
    certificate_number = serializers.CharField(source='certificate.number', read_only=True)
    owner_name = serializers.CharField(source='owner.name', read_only=True)

    class Meta:
        model = Score
        fields = ['id', 'owner_name', 'certificate_number', 'criterion', 'score']



# Сериализатор для модели сертификата
class CertificateSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer(read_only=True)  # Полная информация о владельце
    role = serializers.CharField(source='role.name', read_only=True)  # Человекочитаемая роль
    skills = SkillSerializer(many=True, read_only=True)  # Человекочитаемые навыки
    scores = ScoreSerializer(many=True, read_only=True)
    owner_scores = serializers.SerializerMethodField()  # Добавляем поле для баллов владельца

    def get_owner_scores(self, obj):
        # Баллы владельца, если они подгружены
        return [score.score for score in obj.owner.scores.all()]

    class Meta:
        model = Certificate
        fields = [
            'id', 'number', 'date_issued', 'course_name', 'internship_start_date', 'internship_end_date',
            'owner', 'role', 'skills', 'scores', 'owner_scores'
        ]
