from django.contrib import admin
from .models import *
from django.contrib.admin.widgets import FilteredSelectMultiple


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email')
    search_fields = ('name', 'last_name', 'email')


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('number', 'owner', 'role', 'date_issued', 'course_name',
                    'internship_start_date', 'internship_end_date')
    search_fields = ('number', 'owner',)
    list_filter = ('date_issued',)

    # В
    list_display_links = ('number', 'owner')

    # Фильтры для поля "skills"
    filter_horizontal = ('skills',)

    # FilterSelectMultiple для улучшения интерфейса выбора
    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple('Навыки', is_stacked=False)},
    }


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name', 'category')


class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(SkillCategory, SkillCategoryAdmin)
admin.site.register(Role, RoleAdmin)
