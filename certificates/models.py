from django.db import models
import uuid

class Certificate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID для уникального идентификатора
    certificate_number = models.CharField(max_length=50, unique=True)  # Номер сертификата
    owner_name = models.CharField(max_length=100)  # Имя владельца
    owner_email = models.EmailField(max_length=100, db_index=True)  # Электронный адрес владельца с индексом
    date_issued = models.DateField()  # Дата выдачи сертификата
    expiration_date = models.DateField(null=True, blank=True)  # Дата истечения сертификата (nullable)
    course_name = models.CharField(max_length=150)  # Название курса
    instructor_name = models.CharField(max_length=100)  # Имя инструктора
    organization_name = models.CharField(max_length=150)  # Организация, выдавшая сертификат

    def __str__(self):
        return f"Certificate {self.certificate_number} - {self.owner_name}"

    class Meta:
        indexes = [
            models.Index(fields=['owner_email']),  # Индекс для быстрого поиска по email владельца
        ]
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



