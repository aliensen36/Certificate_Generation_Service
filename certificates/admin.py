from django.contrib import admin
from .models import Certificate, Skill, CertificateSkill

# Регистрируем модель Certificate
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('certificate_number', 'owner_name', 'owner_email', 'date_issued', 'expiration_date', 'course_name', 'instructor_name', 'organization_name')
    search_fields = ('certificate_number', 'owner_name', 'owner_email')
    list_filter = ('date_issued', 'expiration_date')

# Регистрируем модель Skill
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Регистрируем модель CertificateSkill
class CertificateSkillAdmin(admin.ModelAdmin):
    list_display = ('certificate', 'skill')
    search_fields = ('certificate__certificate_number', 'skill__name')
    list_filter = ('certificate', 'skill')

# Регистрация моделей в админке
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(CertificateSkill, CertificateSkillAdmin)
