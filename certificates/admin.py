from django.contrib import admin
from .models import *


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email')
    search_fields = ('name', 'last_name', 'email')


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'owner', 'role', 'date_issued', 'course_name',
                    'internship_start_date', 'internship_end_date')
    search_fields = ('number', 'owner',)
    list_filter = ('date_issued',)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CertificateSkillAdmin(admin.ModelAdmin):
    list_display = ('certificate', 'skill')
    search_fields = ('certificate__number', 'skill__name')
    list_filter = ('certificate', 'skill')


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(CertificateSkill, CertificateSkillAdmin)
