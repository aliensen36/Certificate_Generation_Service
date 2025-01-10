from django.db import models
import uuid


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
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"


# Модель сертификата
class Certificate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=50, unique=True, verbose_name='Номер')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='certificates', verbose_name='Владелец')
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Роль')
    date_issued = models.DateField(verbose_name='Дата выдачи')
    course_name = models.CharField(max_length=150, verbose_name='Название курса')
    internship_start_date = models.DateField(null=True, blank=True, verbose_name="Дата начала стажировки")
    internship_end_date = models.DateField(null=True, blank=True, verbose_name="Дата окончания стажировки")
    skills = models.ManyToManyField(Skill, related_name="certificates", verbose_name="Навыки")

    def __str__(self):
        return f"Certificate {self.number} - {self.owner}"

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'
