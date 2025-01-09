from django.db import models
import uuid


# Перечисление ролей для указания в сертификате
ROLE_CHOICES = [
    ('data_scientist', 'Data Scientist'),
    ('python_developer', 'Python Developer'),
    ('web_developer', 'Web Developer'),
    ('frontend_developer', 'Frontend Developer'),
    ('backend_developer', 'Backend Developer'),
    ('full_stack_developer', 'Full Stack Developer'),
    ('devops_engineer', 'DevOps Engineer'),
    ('software_engineer', 'Software Engineer'),
    ('cloud_engineer', 'Cloud Engineer'),
    ('machine_learning_engineer', 'Machine Learning Engineer'),
    ('qa_engineer', 'QA Engineer'),  # Тестировщик
]

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


# Модель сертификата
class Certificate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=50, unique=True, verbose_name='Номер сертификата')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='certificates', verbose_name='Владелец')
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, blank=True, null=True, verbose_name='Роль')
    date_issued = models.DateField(verbose_name='Дата выдачи сертификата')
    course_name = models.CharField(max_length=150, verbose_name='Название курса')
    organization_name = models.CharField(max_length=150)  # Организация, выдавшая сертификат
    internship_start_date = models.DateField(null=True, blank=True, verbose_name="Дата начала стажировки")
    internship_end_date = models.DateField(null=True, blank=True, verbose_name="Дата окончания стажировки")

    def __str__(self):
        return f"Certificate {self.certificate_number} - {self.owner}"

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'


class Skill(models.Model):
    id = models.BigAutoField(primary_key=True)  # Уникальный идентификатор для навыка
    name = models.CharField(max_length=100, unique=True)  # Название навыка (уникальное)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'


class CertificateSkill(models.Model):
    id = models.BigAutoField(primary_key=True)  # Уникальный идентификатор для связи
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE)  # Ссылка на сертификат
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)  # Ссылка на навык

    def __str__(self):
        return f"Certificate {self.certificate.certificate_number} - Skill {self.skill.name}"

    class Meta:
        verbose_name = 'Навык сертификата'
        verbose_name_plural = 'Навыки сертификатов'



