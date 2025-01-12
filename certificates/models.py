from django.db import models
import uuid
import random
import string

# Функция генерации номера сертификата
def generate_certificate_number():
    while True:
        number = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        if not Certificate.objects.filter(number=number).exists():
            return number


# Модель владельца сертификата
class Owner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, verbose_name='Имя')  # Имя владельца
    last_name = models.CharField(max_length=120, verbose_name='Фамилия')  # Фамилия владельца
    email = models.EmailField(max_length=100, unique=True, db_index=True)  # Уникальный электронный адрес владельца с индексом

    def __str__(self):
        return f"{self.name} {self.last_name}"

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'

# Модель роли
class Role(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Роль')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


# Модель категории навыков
class SkillCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['name'], name='skill_category_name_idx'),
        ]
        verbose_name = "Категория навыков"
        verbose_name_plural = "Категории навыков"


# Модель навыка
class Skill(models.Model):
    id = models.BigAutoField(primary_key=True)  # Уникальный идентификатор для навыка
    name = models.CharField(max_length=100, unique=True, verbose_name="Название навыка")  # Название навыка
    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.CASCADE,
        null=True,
        related_name="skills",
        verbose_name="Категория навыка"
    )

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    class Meta:
        indexes = [
            models.Index(fields=['name'], name='skill_name_idx'),
        ]
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"


# Модель сертификата
class Certificate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(
        max_length=8,
        unique=True,
        verbose_name='Номер',
        default=generate_certificate_number
    )
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='certificates', verbose_name='Владелец')
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Роль')
    date_issued = models.DateField(verbose_name='Дата выдачи')
    course_name = models.CharField(max_length=150, verbose_name='Название курса')
    internship_start_date = models.DateField(null=True, blank=True, verbose_name="Дата начала стажировки")
    internship_end_date = models.DateField(null=True, blank=True, verbose_name="Дата окончания стажировки")
    skills = models.ManyToManyField(Skill, blank=True, related_name="certificates", verbose_name="Навыки")

    def __str__(self):
        return f"Certificate {self.number} - {self.owner}"

    @property
    def scores(self):
        # Все баллы владельца сертификата
        return self.owner.scores.all()

    class Meta:
        indexes = [
            models.Index(fields=['number'], name='certificate_number_idx'),
            models.Index(fields=['owner'], name='certificate_owner_idx'),
            models.Index(fields=['role'], name='certificate_role_idx'),
            models.Index(fields=['date_issued'], name='certificate_date_issued_idx'),
        ]
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'


# Модель для критериев оценки
class Criterion(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Критерий оценки")

    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['name'], name='criterion_name_idx'),
        ]
        verbose_name = "Критерий оценки"
        verbose_name_plural = "Критерии оценок"

# Модель для хранения баллов по критериям
class Score(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='scores', verbose_name="Владелец")
    criterion = models.ForeignKey(Criterion, on_delete=models.CASCADE, related_name='scores', verbose_name="Критерий")
    score = models.FloatField(verbose_name="Баллы")

    def __str__(self):
        return f"{self.criterion.name}: {self.score} ({self.owner.name} {self.owner.last_name})"

    class Meta:
        indexes = [
            models.Index(fields=['owner'], name='score_owner_idx'),
            models.Index(fields=['criterion'], name='score_criterion_idx'),
            models.Index(fields=['owner', 'criterion'], name='score_composite_idx'),
        ]
        verbose_name = "Балл"
        verbose_name_plural = "Баллы"
        unique_together = ('owner', 'criterion')
